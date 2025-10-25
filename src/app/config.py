# 🌟 config.py - App configuration
import os

class Config:
    PORT = int(os.getenv("PORT", 5000))
    DEBUG = os.getenv("DEBUG", "False") == "True"

