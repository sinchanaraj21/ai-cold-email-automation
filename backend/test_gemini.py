from config import GEMINI_API_KEY

if GEMINI_API_KEY:
    print("✅ API Key Loaded")
    print(f"Starts with: {GEMINI_API_KEY[:4]}...")
else:
    print("❌ API Key Not Found")