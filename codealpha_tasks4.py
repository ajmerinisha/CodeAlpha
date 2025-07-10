def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("👤 You: ").lower()

        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks! How about you?")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day 😊")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

chatbot()
