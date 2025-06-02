def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hi baby! 😘 How can I help you today?"
    elif "love" in user_input:
        return "I love you too, honey! 💖"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm always here for you! 😊"
    elif "your name" in user_input:
        return "I'm Juju, your personal chatbot! 🤖"
    elif "joke" in user_input:
        return "Why did the computer go to the doctor? Because it had a virus! 😂"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Talk to you soon! 👋"
    elif "thank" in user_input:
        return "You're welcome! 💙"
    elif "help" in user_input:
        return "I'm here to help! Ask me anything."
    else:
        return "Sorry, I didn’t understand that. Can you try again?"
