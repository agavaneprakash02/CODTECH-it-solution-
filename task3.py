import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! What can I do for you?",
    "how are you": "I am doing great. Thanks for asking!",
    "what is your name": "I am an AI chatbot.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "bye": "Goodbye! Have a nice day."
}

def chatbot_response(user_input):
    tokens = word_tokenize(user_input.lower())
    processed_input = " ".join(tokens)

    for key in responses:
        if key in processed_input:
            return responses[key]

    return "Sorry, I did not understand your question."

print("AI Chatbot is running (type 'bye' to exit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye! 👋")
        break

    print("Bot:", chatbot_response(user_input))
