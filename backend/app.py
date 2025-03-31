from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Initialize Gemini model
model = init_chat_model("llama3-8b-8192", model_provider="groq")

@app.route('/check', methods=['POST'])
def check_text():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    prompt = f"check this for AI Generated content :\n\n{text}\n\nRespond with either true or false."
    
    try:
        result = model.invoke(prompt)
        return jsonify({"result": result.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
