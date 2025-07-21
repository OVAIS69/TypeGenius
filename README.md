# TypeGenius
TypeGenius is a typing speed testing application build in python
This is a web-based typing speed test application that allows users to practice typing with pre-defined passages or generate custom passages using the Google Gemini AI.

The application consists of two main parts:

Frontend: An HTML, CSS, and JavaScript application that runs in the browser.

Backend: A Python Flask application that handles requests for AI-generated text using the Gemini API.

Features
Typing Speed Metrics: Displays Words Per Minute (WPM), Characters Per Minute (CPM), and elapsed time.

Accuracy Tracking: Shows typing accuracy as a percentage.

Visual Feedback: Highlights correct, incorrect, and current characters.

Auditory Feedback: Provides distinct sounds for correct/incorrect key presses and test completion.

Multiple Passages: Choose from a selection of pre-defined typing passages.

AI-Generated Custom Text: Generate unique typing passages based on your prompts using the Google Gemini API.

Project Structure
typing-test-app/
├── index.html          # Frontend: HTML, CSS, and JavaScript for the web application
├── app.py              # Backend: Flask application to handle AI text generation
├── requirements.txt    # Python dependencies for the Flask backend
└── README.md           # This file


Setup and Local Run
To run this application locally, you need to set up both the backend and the frontend.

Prerequisites
Python 3.7+

A Google Gemini API Key. You can obtain one from Google AI Studio.

1. Backend Setup (app.py)
The backend is a Flask application that serves the AI text generation.

Navigate to the project directory:

cd typing-test-app


Create a virtual environment (recommended):

python -m venv venv


Activate the virtual environment:

macOS/Linux:

source venv/bin/activate


Windows (Command Prompt):

venv\Scripts\activate.bat


Windows (PowerShell):

.\venv\Scripts\Activate.ps1


Install Python dependencies:

pip install -r requirements.txt


Set your Gemini API Key:
The app.py expects your Gemini API key to be set as an environment variable named GEMINI_API_KEY.

macOS/Linux:

export GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"


Windows (Command Prompt)::

set GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"


Windows (PowerShell):

$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"


Replace "YOUR_GEMINI_API_KEY_HERE" with your actual API key.

Run the Flask backend:

python app.py


You should see output indicating that the Flask development server is running, typically on http://127.0.0.1:5000/. Keep this terminal window open.

2. Frontend Setup (index.html)
The frontend is a static HTML file that you can open directly in your browser.

Open index.html:
Simply open the index.html file in your preferred web browser (e.g., Chrome, Firefox, Edge). You can do this by double-clicking the file or by right-clicking and choosing "Open with...".

Using the Application
Once both the Flask backend is running and index.html is open in your browser, the typing test should be active.

You can select pre-defined texts from the dropdown.

To generate custom text, click the "✨ Generate New Text" button, enter your prompt in the modal, and click "Generate". The application will then use your running Flask backend to call the Gemini API and provide a new typing passage.

Deployment (Optional)
To make this application accessible online, you would need to deploy the Flask backend to a cloud hosting provider (e.g., Heroku, Google Cloud Platform, AWS, PythonAnywhere) and then host the index.html file (e.g., on GitHub Pages or alongside your backend). Remember to update the backendUrl variable in index.html to your deployed backend's URL.
