# protektalk_app/models.py

from django.db import models
from django.contrib.auth.models import User # Django's built-in User model

class Child(models.Model):
    """
    Represents a child user being monitored.
    Linked to a Django User for potential login/authentication.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Linked Django user account for login")
    nickname = models.CharField(max_length=100, help_text="In-game nickname or preferred name of the child")
    # For a full system, you might link to a specific Parent/Guardian model,
    # but for a demo, linking to another User instance is sufficient.
    parent_guardian = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='supervised_children', null=True, blank=True, help_text="The parent/guardian supervising this child")

    def __str__(self):
        return self.nickname

class Conversation(models.Model):
    """
    Represents an ongoing conversation between a specific child and a specific stranger.
    Stores the AI-generated summary that acts as the conversation history for the LLM.
    """
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='conversations', help_text="The child involved in this conversation")
    stranger_identifier = models.CharField(max_length=255, help_text="A unique identifier for the stranger (e.g., their in-game username, ID)")
    
    # This field is crucial: it stores the AI-generated summary of the conversation
    # which is passed back to the LLM to maintain context.
    ai_summary = models.TextField(blank=True, help_text="AI-generated summary of the conversation history for context")
    
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the conversation record was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the conversation record was last updated")

    class Meta:
        # Ensures that a child has only one active conversation with a specific stranger at a time
        unique_together = ('child', 'stranger_identifier') 
        verbose_name = "Conversation"
        verbose_name_plural = "Conversations"

    def __str__(self):
        return f"Conversation: {self.child.nickname} with {self.stranger_identifier}"

class Message(models.Model):
    """
    Stores individual chat messages within a conversation.
    """
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages', help_text="The conversation this message belongs to")
    sender_type = models.CharField(max_length=10, choices=[('child', 'Child'), ('stranger', 'Stranger')], help_text="Who sent the message: 'child' or 'stranger'")
    content = models.TextField(help_text="The actual text content of the message")
    timestamp = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the message was recorded")

    class Meta:
        ordering = ['timestamp'] # Ensure messages are retrieved in chronological order
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return f"{self.sender_type.capitalize()}: {self.content[:50]}..." # Show first 50 chars

class Alert(models.Model):
    """
    Records an alert triggered by the AI, indicating potential harmful behavior.
    """
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='alerts', help_text="The conversation that triggered this alert")
    alert_type = models.CharField(max_length=10, choices=[('Red', 'Red Flag'), ('Yellow', 'Yellow Flag')], help_text="Type of alert: 'Red' for immediate threat, 'Yellow' for suspicious behavior")
    explanation = models.TextField(help_text="Brief explanation from the AI about why the alert was triggered")
    triggered_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the alert was triggered")
    
    # Fields for tracking notification status (for a full system)
    parent_notified = models.BooleanField(default=False, help_text="Has the parent/guardian been notified?")
    authorities_notified = models.BooleanField(default=False, help_text="Have authorities been notified?")

    class Meta:
        verbose_name = "Alert"
        verbose_name_plural = "Alerts"
        ordering = ['-triggered_at'] # Order alerts by most recent first

    def __str__(self):
        return f"{self.alert_type} Alert for {self.conversation.child.nickname} with {self.conversation.stranger_identifier} at {self.triggered_at.strftime('%Y-%m-%d %H:%M')}"