from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from .models import Message, Conversation
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from textblob import TextBlob
import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)

def a_page(request):
    return render(request, 'chat/a.html')

def welcome_page(request):
    print("DEBUG: welcome_page view called")  # Added debug print
    logger.info(f"Accessed welcome_page, user authenticated: {request.user.is_authenticated}")
    logger.info("Rendering welcome.html template.")
    if request.user.is_authenticated:
        return redirect('conversation_list')
    return render(request, 'chat/welcome.html')

def user_login(request):
    logger.info(f"Accessed user_login, user authenticated: {request.user.is_authenticated}")
    if request.user.is_authenticated:
        return redirect('conversation_list')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('conversation_list')
        else:
            return render(request, 'chat/login.html', {'error': 'Invalid credentials'})
    return render(request, 'chat/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def conversation_list(request):
    conversations = request.user.conversations.all()
    return render(request, 'chat/conversation_list.html', {'conversations': conversations})

from django.shortcuts import redirect

@login_required
def chat_room(request, conversation_id):
    # Redirect chat_room URL to conversation_list for unified AJAX single-page chat UI
    return redirect('conversation_list')

'''
@login_required
def chat_room(request, conversation_id):
    try:
        conversation = get_object_or_404(Conversation, id=conversation_id)
    except Exception as e:
        logger.error(f"Error retrieving conversation: {e}")
        return redirect('conversation_list')
    
    if request.user not in conversation.participants.all():
        return redirect('conversation_list')
    
    messages = conversation.messages.order_by('timestamp')
    other_participants = conversation.participants.exclude(id=request.user.id)
    
    return render(request, 'chat/chat_room.html', {
        'conversation': conversation,
        'messages': messages,
        'other_participants': other_participants,
    })
'''
@login_required
def send_message(request, conversation_id):
    logger.info(f"send_message called with method {request.method} by user {request.user}")
    if request.method == 'POST':
        conversation = get_object_or_404(Conversation, id=conversation_id)
        if request.user not in conversation.participants.all():
            logger.warning(f"Unauthorized send_message attempt by user {request.user} for conversation {conversation_id}")
            return JsonResponse({'error': 'Unauthorized'}, status=403)
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                content = data.get('content', '')
            else:
                content = request.POST.get('content', '')
        except Exception as e:
            logger.error(f"Error parsing send_message data: {e}")
            return JsonResponse({'error': 'Invalid data'}, status=400)

        # Sentiment analysis
        blob = TextBlob(content)
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            sentiment = 'Positive'
        elif polarity < -0.1:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        message = Message.objects.create(conversation=conversation, sender=request.user, content=content, sentiment=sentiment)
        logger.info(f"Message created with id {message.id} in conversation {conversation_id} by user {request.user}")
        return JsonResponse({
            'success': True,
            'message': {
                'sender': message.sender.username,
                'content': message.content,
                'sentiment': message.sentiment,
                'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            }
        })
    logger.warning(f"Invalid request method {request.method} for send_message by user {request.user}")
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def new_conversation(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            other_user = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, 'chat/new_conversation.html', {'error': 'User not found'})
        if other_user == request.user:
            return render(request, 'chat/new_conversation.html', {'error': 'Cannot start conversation with yourself'})
        # Check if conversation already exists
        conversations = request.user.conversations.filter(participants=other_user)
        if conversations.exists():
            conversation = conversations.first()
        else:
            conversation = Conversation.objects.create()
            conversation.participants.add(request.user, other_user)
        return redirect('conversation_list')
    return render(request, 'chat/new_conversation.html')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('conversation_list')
            else:
                messages.error(request, "Authentication failed after registration.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})
