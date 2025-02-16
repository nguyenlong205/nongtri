from flask import Flask, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI

app = Flask(__name__)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key="AIzaSyDt3AbmnJS1JIYGuG7fJk-bm75wCJn8f8U")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_input = data.get("question", "")
    if not user_input:
        return jsonify({"error": "Missing question"}), 400

    response = "".join(chunk.content for chunk in llm.stream(user_input))
    return jsonify({"response": response})

@app.route("/", methods=["GET"])
def home():
    return "Chat server is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    
