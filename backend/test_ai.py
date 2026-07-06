from ai_email_generator import generate_ai_email

print("Step 1: Starting")

prompt = """
Write a short professional greeting for a recruiter.
Keep it under 30 words.
"""

print("Step 2: Calling Gemini")

response = generate_ai_email(prompt)

print("Step 3: Response received")

print(response)