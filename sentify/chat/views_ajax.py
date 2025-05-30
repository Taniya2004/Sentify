from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Conversation, Message

@login_required
def chat_messages(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    if request.user not in conversation.participants.all():
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    participants = [user.username for user in conversation.participants.all()]
    messages_qs = Message.objects.filter(conversation=conversation).order_by('timestamp')
    messages = []
    for msg in messages_qs:
        messages.append({
            'content': msg.content,
            'timestamp': msg.timestamp.strftime('%H:%M'),
            'timestamp_iso': msg.timestamp.isoformat() if msg.timestamp else None,
            'sentiment': msg.sentiment if hasattr(msg, 'sentiment') else '',
            'is_sender': msg.sender == request.user,
        })

    return JsonResponse({
        'participants': participants,
        'messages': messages,
    })
