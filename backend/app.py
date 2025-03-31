from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

@app.route('/check', methods=['POST'])
def check_text():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    prompt = f"Determine if the following text is written by a human or an AI:\n\n{text}\n\nRespond with 'AI' or 'Human'."
    
    try:
        result = model.invoke(prompt)
        return jsonify({"result": result.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
