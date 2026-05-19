from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
print("Loaded API Key:", API_KEY)

# Create a client with your API key
client = genai.Client(api_key=API_KEY)

# Pick a model
model = "models/gemini-2.5-flash"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_response():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"})

    try:
    # Send message to Gemini
        response = client.models.generate_content(
        model=model,
        contents=user_message
        )

    # ✅ Extract text from candidates
        if response.candidates:
            reply = response.candidates[0].content.parts[0].text
        else:
            reply = "No response generated."

        print("RAW RESPONSE:", reply)
        return jsonify({"reply": reply})


    except Exception as e:
        print("FULL ERROR:", e)
        return jsonify({"reply": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
