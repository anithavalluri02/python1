# 🌟 __init__.py - Initializes the Flask application

from flask import Flask
from app.routes import register_routes
from app.config import Config

def create_app():
    """Factory pattern to create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)
    register_routes(app)
    return app

