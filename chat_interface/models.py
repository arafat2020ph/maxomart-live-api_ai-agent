from django.db import models

# Create your models here.
from django.db import models
from api_client.models import ChatSession # Importing from api_client app

class ChatLog(models.Model):
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='logs')
    role = models.CharField(max_length=20) # 'user' or 'assistant'
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']