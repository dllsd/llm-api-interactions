import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("API key not found")

client = genai.Client(api_key=API_KEY)

def ask_llm(prompt):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text



if __name__ == "__main__":
    print("LLM Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        reply = ask_llm(user_input)
        print("AI:", reply)
        print()