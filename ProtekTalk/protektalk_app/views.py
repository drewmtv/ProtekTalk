# protektalk_app/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Child, Conversation, Message, Alert
from .gemini_api_client import ProtekTalkAIManager # <--- Updated import
from django.contrib.auth.models import User 

# Initialize the AI Manager globally or as a class attribute if using Class-Based Views
ai_manager = ProtekTalkAIManager()

@method_decorator(csrf_exempt, name='dispatch') 
def process_chat(request):
    """
    API endpoint to receive chat messages, analyze them with AI,
    and store conversation data and alerts.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            child_nickname = data.get('child_nickname')
            stranger_identifier = data.get('stranger_identifier')
            child_message = data.get('child_message')
            stranger_message = data.get('stranger_message')
            game_context = data.get('game_context', 'an online multiplayer game') 

            if not all([child_nickname, stranger_identifier, child_message, stranger_message]):
                return JsonResponse({'status': 'error', 'message': 'Missing required fields (child_nickname, stranger_identifier, child_message, stranger_message)'}, status=400)

            # --- Database Operations ---

            try:
                child = Child.objects.get(nickname=child_nickname)
            except Child.DoesNotExist:
                dummy_username = f"child_{child_nickname.replace(' ', '_').lower()}"
                user, created_user = User.objects.get_or_create(username=dummy_username, defaults={'password': 'dummy_password_for_demo'})
                child = Child.objects.create(nickname=child_nickname, user=user)
                print(f"Created new child: {child_nickname} with user: {user.username}")


            conversation, created_conversation = Conversation.objects.get_or_create(
                child=child,
                stranger_identifier=stranger_identifier,
                defaults={'ai_summary': ''} 
            )

            conversation_tracker = conversation.ai_summary

            # --- AI Interaction ---

            # Call the AI Service
            ai_response = ai_manager.analyze_conversation(
                conversation_tracker=conversation_tracker,
                child_message=child_message,
                stranger_message=stranger_message,
                game_context=game_context
            )

            # --- Save Messages (regardless of AI outcome) ---
            Message.objects.create(conversation=conversation, sender_type='child', content=child_message)
            Message.objects.create(conversation=conversation, sender_type='stranger', content=stranger_message)

            # --- Process AI Response and Update Database ---
            response_data = {'status': ai_response['status']}
            
            if ai_response['status'] in ['Red', 'Yellow']:
                Alert.objects.create(
                    conversation=conversation,
                    alert_type=ai_response['status'],
                    explanation=ai_response['explanation']
                )
                response_data['alert_type'] = ai_response['status']
                response_data['explanation'] = ai_response['explanation']
                
                print(f"!!! PROTEKTALK ALERT: {ai_response['status']} - {ai_response['explanation']} for {child_nickname} and {stranger_identifier}")
            
            elif ai_response['status'] == 'Safe':
                conversation.ai_summary = ai_response['summary']
                conversation.save()
                response_data['summary'] = ai_response['summary']
                print(f"Conversation safe. Summary updated for {child_nickname} and {stranger_identifier}.")
            
            else: 
                response_data['message'] = ai_response.get('explanation', 'Unknown AI processing error.')
                return JsonResponse(response_data, status=500) 

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON in request body'}, status=400)
        except Exception as e:
            print(f"An unexpected error occurred in process_chat: {e}")
            return JsonResponse({'status': 'error', 'message': f'An internal server error occurred: {e}'}, status=500)