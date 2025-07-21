import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # Loads GEMINI_API_KEY from .env

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ GEMINI_API_KEY not set in .env")
    exit()

genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    response = model.generate_content("Give a short summary of the Indian IT industry.")
    print("✅ Gemini API is working!")
    print("AI Output:\n", response.text)
except Exception as e:
    print("❌ Gemini API failed:")
    print(e)
