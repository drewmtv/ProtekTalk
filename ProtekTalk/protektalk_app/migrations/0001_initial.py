# Generated by Django 5.2 on 2025-05-22 17:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(help_text='In-game nickname or preferred name of the child', max_length=100)),
                ('parent_guardian', models.ForeignKey(blank=True, help_text='The parent/guardian supervising this child', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervised_children', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(help_text='Linked Django user account for login', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stranger_identifier', models.CharField(help_text='A unique identifier for the stranger (e.g., their in-game username, ID)', max_length=255)),
                ('ai_summary', models.TextField(blank=True, help_text='AI-generated summary of the conversation history for context')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the conversation record was created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Timestamp when the conversation record was last updated')),
                ('child', models.ForeignKey(help_text='The child involved in this conversation', on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to='protektalk_app.child')),
            ],
            options={
                'verbose_name': 'Conversation',
                'verbose_name_plural': 'Conversations',
                'unique_together': {('child', 'stranger_identifier')},
            },
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_type', models.CharField(choices=[('Red', 'Red Flag'), ('Yellow', 'Yellow Flag')], help_text="Type of alert: 'Red' for immediate threat, 'Yellow' for suspicious behavior", max_length=10)),
                ('explanation', models.TextField(help_text='Brief explanation from the AI about why the alert was triggered')),
                ('triggered_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the alert was triggered')),
                ('parent_notified', models.BooleanField(default=False, help_text='Has the parent/guardian been notified?')),
                ('authorities_notified', models.BooleanField(default=False, help_text='Have authorities been notified?')),
                ('conversation', models.ForeignKey(help_text='The conversation that triggered this alert', on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='protektalk_app.conversation')),
            ],
            options={
                'verbose_name': 'Alert',
                'verbose_name_plural': 'Alerts',
                'ordering': ['-triggered_at'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_type', models.CharField(choices=[('child', 'Child'), ('stranger', 'Stranger')], help_text="Who sent the message: 'child' or 'stranger'", max_length=10)),
                ('content', models.TextField(help_text='The actual text content of the message')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the message was recorded')),
                ('conversation', models.ForeignKey(help_text='The conversation this message belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='protektalk_app.conversation')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ['timestamp'],
            },
        ),
    ]
