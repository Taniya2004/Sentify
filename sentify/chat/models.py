from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id} - Participants: {', '.join([user.username for user in self.participants.all()])}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages', null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    sentiment = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} ({self.sentiment}): {self.content[:20]}"