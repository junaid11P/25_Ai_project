# Import the regular expressions module to handle pattern matching
import re

# A dictionary that maps keywords to predefined responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! What can I do for you?",
    "greetings": "Greetings! How may I help you?",
    "what's your name": "I am a simple chatbot created to assist you.",
    "who are you": "I am a chatbot designed to help with your queries.",
    "what can you do": "I can answer simple questions and provide predefined responses.",
    "how are you": "I'm just a program, but thanks for asking! How can I help you?",
    "bye": "Goodbye! Have a great day!",
    "help": "Sure! What do you need help with?",
    "thank you": "You're welcome! If you have more questions, feel free to ask.",
    "thanks": "No problem! I'm here to help.",
    "sorry": "No worries! How can I assist you further?",
    "yes": "Great! What would you like to know?",
    "no": "Okay! If you change your mind, feel free to ask.",
    "maybe": "That's fine! Let me know if you have any questions later.",
    "please": "Of course! How can I assist you?",
    "goodbye": "Goodbye! Take care!",
    "good morning": "Good morning! How can I assist you today?",
    "good afternoon": "Good afternoon! What can I do for you?",
    "good evening": "Good evening! How may I help you?",
    "default": "I'm sorry, I didn't understand that. Can you please rephrase?"
}

# Function to get a response based on user input
def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]
        
    return responses["default"]

# Main function to run the chatbot
def chatbot():
    print("Chatbot: Hello! I'm here to assist you. (type 'bye' to exit)")

    while True:

    # Get user input
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        # Get the chatbot's response based on user input
        response = chatbot_response(user_input)

        #Print the chatbot's response
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()