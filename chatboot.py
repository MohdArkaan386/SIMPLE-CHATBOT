# chatbot.py
def chatbot():
    print("Chatbot ready! Type 'exit' to quit.")
    while True:
        user = input("You: ").lower()
        if user == "exit":
            break
        elif "hello" in user:
            print("Bot: Hi there!")
        elif "how are you" in user:
            print("Bot: I'm doing great, thanks!")
        elif "bye" in user:
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
