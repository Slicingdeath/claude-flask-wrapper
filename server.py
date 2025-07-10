from flask import Flask, render_template, request, jsonify
from claude_api import get_llm_response
from dotenv import load_dotenv

# Intialize Flask
app = Flask(__name__)

# Load env variables
load_dotenv()

@app.route('/')
def home():
    """Serve the chat interface"""
    return render_template("index.html")

@app.route('/chat', mehtods=['POST'])
def chat():
    """Handle chat messages"""
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    response = get_llm_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)