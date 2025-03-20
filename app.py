from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/api/v1/demo')
def demo():
    return jsonify({
        "message": "Hello from ECS!",
        "environment": os.getenv("ENVIRONMENT", "development")
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#pgft