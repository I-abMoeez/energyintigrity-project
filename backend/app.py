from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend running on Vercel!"

# Vercel handler
def handler(request, response):
    return app(request.environ, lambda *args: None)