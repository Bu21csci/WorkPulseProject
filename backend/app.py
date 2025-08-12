from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

activity_logs = []

# Root route to check if backend is running
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "✅ WorkPulse Backend is Running!"})

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json
    print("Received:", data)
    data['received_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    activity_logs.append(data)
    return jsonify({"status": "success"})

@app.route('/logs', methods=['GET'])
def logs():
    return jsonify(activity_logs)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
