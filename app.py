from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Jarvis Online"

@app.route('/message', methods=['POST'])
def message():
    data = request.json
    user_input = data.get("text", "")

    reply = f"Jarvis heard: {user_input}"

    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
