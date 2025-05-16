from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ add this
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)  # ✅ allow cross-origin requests

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided."}), 400

    try:
        #reply = f"(Test reply) You said: {user_input}"

        /response = openai.ChatCompletion.create(#
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for SharePoint users."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message["content"]#
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "Chatbot is Live!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
