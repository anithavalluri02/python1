# 🌟 routes.py - Define API endpoints
from flask import jsonify

def register_routes(app):
    @app.route("/")
    def home():
        return jsonify({"message": "Hello, Kubernetes!"})  # 💚 Home endpoint

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy"})  # ✅ Health check

