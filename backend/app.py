from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

activity_logs = []

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
    app.run(debug=True)
