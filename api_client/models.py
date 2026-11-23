from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class ChatSession(models.Model):
    user_identifier = models.CharField(max_length=100, help_text="MaxoMart user ID or Email")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session {self.id} - {self.user_identifier}"

class ChatMessage(models.Model):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('assistant', 'Assistant'),
        ('system', 'System'),
    ]
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

class CartItem(models.Model):
    user_identifier = models.CharField(max_length=100)
    product_id = models.CharField(max_length=50)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price_cents = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity}x {self.product_name}"