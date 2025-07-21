from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app) # Enable CORS for cross-origin requests from your HTML file

# Configure the Gemini API key
# IMPORTANT: In a real application, never hardcode API keys.
# Use environment variables or a secure configuration management system.
# For this example, we'll assume the API key is set as an environment variable
API_KEY = os.getenv("GEMINI_API_KEY", "") 

# If running in a Canvas environment, the API key might be passed differently.
# For local testing, ensure GEMINI_API_KEY is set in your environment variables.
# Example: export GEMINI_API_KEY="YOUR_API_KEY_HERE"
if not API_KEY:
    # Fallback for Canvas environment where __api_key__ is a global variable
    # This part is specific to how Canvas might inject the API key.
    # For local testing, you'll need to set the environment variable.
    API_KEY = os.getenv("API_KEY", "") # Trying another common environment variable name

genai.configure(api_key=API_KEY)

@app.route('/generate-text', methods=['POST'])
def generate_text():
    """
    Endpoint to generate text using the Gemini API.
    Expects a JSON payload with a 'prompt' field.
    """
    try:
        data = request.get_json()
        user_prompt = data.get('prompt')

        if not user_prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Construct the full prompt for the LLM
        llm_prompt = f"Generate a short, single paragraph (around 50-100 words) for a typing test about: {user_prompt}. Ensure it is grammatically correct and suitable for typing practice."

        # Call the Gemini API
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(llm_prompt)

        if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
            generated_text = response.candidates[0].content.parts[0].text
            return jsonify({"generatedText": generated_text.strip()}), 200
        else:
            return jsonify({"error": "Failed to generate text from LLM."}), 500

    except Exception as e:
        print(f"Error during text generation: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500

if __name__ == '__main__':
    # To run locally:
    # 1. Save this code as app.py
    # 2. Install Flask and google-generativeai: pip install Flask google-generativeai
    # 3. Set your API key as an environment variable: export GEMINI_API_KEY="YOUR_API_KEY_HERE"
    # 4. Run the app: python app.py
    # This will run on http://127.0.0.1:5000/
    app.run(debug=True) # debug=True for development, set to False in production
