# Google Gemini Chatbot
# Run: export GOOGLE_API_KEY="your-google-api-key"
# Get your key at: https://aistudio.google.com/app/apikey

import google.generativeai as genai
import os
import sys

# Get API key from environment variable
api_key ="AIzaSyAHmuS4OgMYpia6IcZiM6rsEwi76Gq-sew"

if not api_key:
    print("ERROR: GOOGLE_API_KEY environment variable not set.")
    print("Set it in terminal using:")
    print('setx GOOGLE_API_KEY "your-google-api-key"')
    sys.exit(1)

# Configure the Gemini API
genai.configure(api_key=api_key)

# Create the model
model = genai.GenerativeModel('gemini-2.5-flash')

# Start a chat session
chat = model.start_chat(history=[])

print("Chatbot: Hey, how are you? (using Gemini 2.5 Flash)")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    #hiiiiiiiiiii
    try:
        response = chat.send_message(user_input)
        print("Chatbot:", response.text)
    except Exception as e:
        print(f"Error: {e}")
# python -m venv .venv
# .venv\Scripts\activate
# pip install google-generative-ai
