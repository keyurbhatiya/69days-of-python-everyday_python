import os
from groq import Groq
import dotenv
dotenv.load_dotenv()

# 1. Initialize the Client
# Sir, remember to set your API key in your environment variables or paste it here
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

def get_ai_response(user_input):
    print("🤖 Jarvis is thinking...")
    
    # 2. Create the Completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are Jarvis, a highly intelligent and witty AI assistant. You address the user as Sir."
            },
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama-3.3-70b-versatile", # Using Llama 3 for maximum speed
        temperature=0.7,
    )

    # 3. Output the result
    response = chat_completion.choices[0].message.content
    return response

if __name__ == "__main__":
    print("--- Day 59: Groq AI Integration ---")
    while True:
        user_query = input("\n👤 You: ")
        if user_query.lower() in ["exit", "quit", "bye"]:
            print("👋 Goodbye, Sir!")
            break
            
        ai_reply = get_ai_response(user_query)
        print(f"\n🤖 Jarvis: {ai_reply}")