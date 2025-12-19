from openai import OpenAI

# ===== OPENAI =====
client = OpenAI(
    api_key="Paste_Your_API_Key"

def chatgpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI chatbot."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# ===== MAIN CHAT LOOP =====
print("🤖 AI Chatbot powered by ChatGPT. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "stop"]:
        print("Chatbot: Goodbye! 👋")
        break
    
    reply = chatgpt_response(user_input)
    print("Chatbot:", reply)

