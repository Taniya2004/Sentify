from django.urls import path
from .views_ajax import chat_messages

urlpatterns = [
    path('chat/messages/<int:conversation_id>/', chat_messages, name='chat_messages'),
]
