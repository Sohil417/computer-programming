# Define a dictionary of questions and answers
qa_dict = {
    "What is your name?": "My name is ChatGPT.",
    "How old are you?": "I am an AI created by OpenAI, so I don't age.",
    "Where do you live?": "I exist in the cloud, so I don't have a physical location.",
    "What can you do?": "I can assist with programming, answer questions, and much more!",
    "What is Python?": "Python is a high-level, interpreted programming language."
}

# Function to get the answer based on the user's question
def get_answer(question):
    return qa_dict.get(question, "Sorry, I don't understand that question.")

# Main program loop
while True:
    print("\nAsk me a question (type 'exit' to quit):")
    user_question = input()

    # Exit condition
    if user_question.lower() == 'exit':
        print("Goodbye!")
        break

    # Retrieve and print the answer
    answer = get_answer(user_question)
    print(f"Answer: {answer}")
