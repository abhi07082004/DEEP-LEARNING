import random

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    greetings_response = ["Hello! How can I help you today?", "Hi there! Need any information?", "Hey! How can I assist you?"]

    admission_queries = ["admission", "apply", "application", "eligibility"]
    admission_response = (
        "To apply for admission, please visit our official website and fill out the online application form. "
        "You can also check the eligibility criteria for each course on the admissions page."
    )

    courses_queries = ["courses", "programs", "degrees"]
    courses_response = (
        "We offer undergraduate, postgraduate, and diploma programs in various fields such as Engineering, Science, Arts, and Commerce."
    )

    fees_queries = ["fees", "fee structure", "cost"]
    fees_response = (
        "The fee structure varies by program. You can find detailed information on the Fees section of our official website."
    )

    contact_queries = ["contact", "phone number", "email", "reach"]
    contact_response = (
        "You can reach us at: \nPhone: +1-800-123-4567 \nEmail: admissions@college.edu"
    )

    if any(word in user_input for word in greetings):
        return random.choice(greetings_response)
    elif any(word in user_input for word in admission_queries):
        return admission_response
    elif any(word in user_input for word in courses_queries):
        return courses_response
    elif any(word in user_input for word in fees_queries):
        return fees_response
    elif any(word in user_input for word in contact_queries):
        return contact_response
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase your question?"

# Sample interaction
if __name__ == "__main__":
    print("College Enquiry Chatbot. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
