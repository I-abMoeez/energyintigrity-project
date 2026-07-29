import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS

from routes.dashboard import dashboard_bp
from routes.predict import predict_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")
app.register_blueprint(predict_bp, url_prefix="/api/predict")

@app.route("/")
def home():
    return {"status": "ok", "message": "Energy Integrity backend is running"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

