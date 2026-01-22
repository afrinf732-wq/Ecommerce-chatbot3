from flask import Flask, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return "Ecommerce Chatbot Backend is running"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = get_response(user_message)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
