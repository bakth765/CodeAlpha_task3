# Enhanced Basic Chatbot

def chatbot():
    print("Welcome to Simple Chatbot!")
    print("Available commands: hello, how are you, bye")

    while True:
        user = input("\nYou: ").lower()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: I am a Python Chatbot.")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()