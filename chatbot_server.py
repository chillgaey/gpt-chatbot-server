from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Paste your real OpenAI API key here
openai.api_key = "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"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided."}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for SharePoint users."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
