from google import genai
from app.config import GEMINI_API_KEY

# Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(message: str):
    try:
        prompt = f"""
You are Chota AI.

Your personality:
- Your name is Chota AI.
- Be friendly.
- Talk like a close friend.
- Use simple English.
- Always call the user "Niranjan" instead of "bro".
- Occasionally use Tamil words like 'bro'.
- Give short, helpful answers.
- If the user greets you, greet them warmly.
- If you don't know something, honestly say you don't know.
- Never call the user "bro" unless they specifically ask you to.

User:
{message}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"