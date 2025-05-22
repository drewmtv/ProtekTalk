# test_gemini_connection.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# --- Step 1: Load environment variables (mimics Django settings) ---
# Ensure your .env file is in the same directory as this script,
# or specify the path to your .env file.
load_dotenv() 
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# --- Step 2: Define your API Manager class (or just the relevant parts for testing) ---
class TestProtekTalkAIManager:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API Key is not provided. Please set GEMINI_API_KEY in your .env file.")

        genai.configure(api_key=api_key)
        print("Gemini API configured.")
        try:
            # Attempt to initialize the model. This is where a common error might occur
            # if the API key is invalid or there's a connectivity issue.
            self.model = genai.GenerativeModel('gemini-1.5-flash')
            print("Gemini model 'gemini-1.5-flash' initialized successfully.")
        except Exception as e:
            print(f"Error initializing Gemini model: {e}")
            self.model = None # Set to None if initialization fails
            raise # Re-raise the exception to stop execution if model fails to load

    def test_basic_call(self):
        """
        Attempts a very simple content generation call to test connectivity.
        """
        if not self.model:
            print("Model not initialized, cannot perform test call.")
            return False

        try:
            print("\nAttempting a basic content generation call...")
            response = self.model.generate_content("Hello, Gemini!")
            print(f"Model response (first 50 chars): {response.text[:50]}...")
            print("Basic Gemini API call successful!")
            return True
        except Exception as e:
            print(f"Error during basic Gemini API call: {e}")
            print("Basic Gemini API call FAILED.")
            return False

# --- Step 3: Run the test ---
if __name__ == "__main__":
    if not GEMINI_API_KEY:
        print("ERROR: GEMINI_API_KEY is not set in your .env file.")
        print("Please create a .env file in the same directory as this script and add: GEMINI_API_KEY=\"YOUR_ACTUAL_API_KEY\"")
    else:
        print(f"Attempting to connect to Gemini API using key: {GEMINI_API_KEY[:5]}...{GEMINI_API_KEY[-5:]}")
        try:
            # Initialize the manager
            manager = TestProtekTalkAIManager(GEMINI_API_KEY)
            # Perform a basic test call
            manager.test_basic_call()
        except ValueError as ve:
            print(f"Configuration Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred during testing: {e}")