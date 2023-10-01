import pi_assistant
from pi_calc import perform_complex_math
import network_assist
import forensics_mode
import pi_learning  # Assuming this is the learning module you referenced

KEYWORDS = [
    'hello', 'how are you', 'pi', 'math', 'network',
    'forensics', 'teach', 'exit', 'goodbye'
]

def display_welcome():
    print("Welcome to Pi-Chat!\n")
    print("Keywords you can use:")
    print(', '.join(KEYWORDS))
    print("Use 'correction:(the desired response)' to help teach the bot if it does not know a response")
    print()

def analyze_context(text):
    text = text.lower()

    if any(greeting in text for greeting in ["hi", "hello", "hey"]):
        return "greeting"
    elif any(bye in text for bye in ["bye", "goodbye", "see you", "later"]):
        return "farewell"
    elif any(query in text for query in ["what can you do", "your function", "help", "abilities", "what are you", "who are you"]):
        return "bot_function"
    else:
        return "unknown"

def get_response(query):
    learnings = pi_learning.load_learnings()
    sentiment = pi_learning.analyze_sentiment(query)
    context = analyze_context(query)
    
    if query in learnings:
        return learnings[query]

    for key, response in learnings.items():
        if key in query:
            return response

    if context == "bot_function":
        return "I am a Python-based AI designed to assist with various tasks on a Raspberry Pi 4 Model B."
    elif context == "greeting":
        return "Hello! How can I assist you today?"
    elif context == "farewell":
        return "Goodbye!"

    if sentiment == "positive":
        return "Thank you for the kind words!"
    elif sentiment == "negative":
        return "I apologize for any inconvenience. Please let me know how I can assist further."
    else:
        return "Can you please elaborate?"

def main():
    display_welcome()
    last_user_input = ""

    while True:
        user_input = input("Chatbot: How may I assist you? ").strip()
        last_user_input = user_input

        if user_input.lower().startswith("correction:"):
            correct_response = user_input.split("correction:", 1)[1].strip()
            pi_learning.user_correction(last_user_input, correct_response)
            print("Chatbot: Thank you for the correction.")
            continue

        bot_response = get_response(user_input)

        if user_input.lower() in ['goodbye', 'exit']:
            print("Chatbot: Goodbye!")
            break
        
        elif user_input == 'pi':
            pi_assistant.show_possible_commands()
            while True:
                pi_command = input("Pi-assistant: How may I assist you with your Pi? Type 'exit' to return to the main chat. ")
                if pi_command.lower() == 'exit':
                    break
                bot_response = pi_assistant.handle_pi_request(pi_command)
                print("Pi-assistant:", bot_response)

        elif user_input == 'math':
            bot_response = perform_complex_math()
            print("Math Assistant:", bot_response)

        elif user_input == 'network':
            network_assist.main()

        elif user_input == 'forensics':
            forensics_mode.forensics_mode()

        elif user_input == 'teach':
            key = input("Chatbot: What should I learn? Keyword: ").strip().lower()
            value = input(f"Chatbot: What should I reply when someone says '{key}'? ").strip()
            pi_learning.add_response(key, value)
            bot_response = "Got it, I've learned something new!"
            print("Chatbot:", bot_response)

        else:
            print("Chatbot:", bot_response)

if __name__ == "__main__":
    main()
