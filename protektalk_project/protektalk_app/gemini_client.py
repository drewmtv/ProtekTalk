import google.generativeai as genai
from django.conf import settings
import re
from .prompt_templates import generate_listener_prompt # Import the prompt generation function

class ProtekTalkAIManager:
    """
    Manages interactions with the Google Gemini API for conversation analysis.
    This class handles API configuration, sending requests, and parsing responses.
    """
    def __init__(self):
        # Ensure the API key is set before configuring the generative AI library
        if not settings.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not set in Django settings. Please add it to your .env file.")
        
        genai.configure(api_key=settings.GEMINI_API_KEY)
        # Initialize the Gemini model you want to use.
        # 'gemini-1.5-flash' is a good choice for cost-effectiveness and speed.
        self.model = genai.GenerativeModel('gemini-1.5-flash') 

    def analyze_conversation(self, conversation_tracker: str, child_message: str, stranger_message: str, game_context: str = "an online multiplayer game") -> dict:
        """
        Sends the constructed prompt to the Gemini model and parses its response.
        
        Args:
            conversation_tracker (str): The summary of previous conversation.
            child_message (str): The latest message from the child.
            stranger_message (str): The latest message from the stranger.
            game_context (str): The context of the game.
            
        Returns:
            dict: A dictionary containing the analysis result, e.g.,
                  {'status': 'Red', 'explanation': '...'}
                  {'status': 'Yellow', 'explanation': '...'}
                  {'status': 'Safe', 'summary': '...'}
                  {'status': 'Error', 'explanation': '...'}
        """
        # Use the imported function to generate the prompt
        prompt = generate_listener_prompt(conversation_tracker, child_message, stranger_message, game_context)
        
        try:
            # Call the Gemini API
            response = self.model.generate_content(prompt)
            raw_text_response = response.text.strip()
            
            # Use regular expressions to parse the AI's output
            # This assumes the AI strictly follows the output format specified in the prompt.
            
            red_match = re.match(r'^(Red):\s*(.*)', raw_text_response, re.IGNORECASE)
            yellow_match = re.match(r'^(Yellow):\s*(.*)', raw_text_response, re.IGNORECASE)

            if red_match:
                return {'status': 'Red', 'explanation': red_match.group(2)}
            elif yellow_match:
                return {'status': 'Yellow', 'explanation': yellow_match.group(2)}
            else:
                # If no "Red:" or "Yellow:" prefix, assume it's a "Safe" summary
                return {'status': 'Safe', 'summary': raw_text_response}

        except Exception as e:
            # Catch any exceptions during API call (e.g., network issues, rate limits, invalid API key)
            print(f"Error calling Gemini API: {e}")
            # In a production system, you'd log this error and potentially have a fallback.
            # For a hackathon demo, returning an 'Error' status is sufficient.
            return {'status': 'Error', 'explanation': f"AI processing failed: {e}. Check API key and rate limits."}