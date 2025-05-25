from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .gemini_client import ProtekTalkAIManager
from .fake_responds import generate_stranger_reply

# Initialize once at the top
ai_manager = ProtekTalkAIManager()

def chat_render(request):
    return render(request, 'protektalk_app/chat.html')

@csrf_exempt  # Optional if you handle CSRF via header
def process_chat(request):
    if request.method == 'POST':
        try:
            # Parse JSON payload
            data = json.loads(request.body)
            child_msg = data.get('child_message', '')
            stranger_msg = data.get('stranger_message', '')
            context = data.get('game_context', '')
            conversation_tracker = ""  # Placeholder: Pull from DB/session/history if applicable

            # Analyze the chat
            ai_result = ai_manager.analyze_conversation(
                conversation_tracker=conversation_tracker,
                child_message=child_msg,
                stranger_message=stranger_msg,
                game_context=context
            )

            # Create a simulated stranger reply
            simulated_stranger_msg = generate_stranger_reply()

            # Construct the response
            response_data = {
                'stranger_reply': simulated_stranger_msg
            }

            # Handle AI result alerts
            if ai_result['status'] in ['Red', 'Yellow']:
                response_data['alert_type'] = ai_result['status']
                response_data['explanation'] = ai_result.get('explanation', 'No explanation provided.')

            return JsonResponse(response_data)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)