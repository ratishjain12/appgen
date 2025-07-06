from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask!"

@app.route("/env")
def env_check():
    return f"ENV: {os.getenv('FLASK_ENV', 'not set')}"
