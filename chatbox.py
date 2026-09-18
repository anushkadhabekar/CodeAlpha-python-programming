print("🤖 ChatBot: Hello! I am a simple chatbot.")
print("🤖 ChatBot: You can ask me something or type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("🤖 ChatBot: Hello! Nice to meet you.")

    elif user_input == "how are you":
        print("🤖 ChatBot: I am doing great! Thank you for asking.")

    elif user_input == "what is your name":
        print("🤖 ChatBot: My name is Python ChatBot.")

    elif user_input == "who are you":
        print("🤖 ChatBot: I am a rule-based chatbot created using Python.")

    elif user_input == "what can you do":
        print("🤖 ChatBot: I can respond to simple questions using predefined rules.")

    elif user_input == "bye":
        print("🤖 ChatBot: Goodbye! Have a nice day! 👋")
        break

    else:
        print("🤖 ChatBot: Sorry, I don't understand that.")