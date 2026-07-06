from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_NAME = os.getenv("PROJECT_NAME")
SENDER_NAME = os.getenv("SENDER_NAME")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PORTFOLIO = os.getenv("PORTFOLIO")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")