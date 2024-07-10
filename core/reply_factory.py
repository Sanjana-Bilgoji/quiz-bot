
from .constants import BOT_WELCOME_MESSAGE, PYTHON_QUESTION_LIST


def generate_bot_responses(message, session):
    bot_responses = []

    current_question_id = session.get("current_question_id")
    if not current_question_id:
        bot_responses.append(BOT_WELCOME_MESSAGE)

    success, error = record_current_answer(message, current_question_id, session)

    if not success:
        return [error]

    next_question, next_question_id = get_next_question(current_question_id)

    if next_question:
        bot_responses.append(next_question)
    else:
        final_response = generate_final_response(session)
        bot_responses.append(final_response)

    session["current_question_id"] = next_question_id
    session.save()

    return bot_responses


def record_current_answer(answer, current_question_id, session):
    '''
    Validates and stores the answer for the current question to django session.
    '''
    return True, ""
    def record_current_answer(answer, current_question_id, session):
    """
    Validates and stores the answer for the current question to the Django session.

    Parameters:
    - answer: The answer provided by the user.
    - current_question_id: The ID of the current question being answered.
    - session: The Django session object where the answer will be stored.

    Returns:
    - Tuple: (boolean, string) indicating success and a message.
    """
    try:
        # Validate the answer (simple validation as an example)
        if not answer:
            return False, "Answer cannot be empty."

        # Store the answer in the session
        session_key = f'question_{current_question_id}_answer'
        session[session_key] = answer
        session.modified = True

        return True, "Answer recorded successfully."
    except Exception as e:
        # Log the exception if necessary
        return False, f"An error occurred: {str(e)}"




def get_next_question(current_question_id):
    '''
    Fetches the next question from the PYTHON_QUESTION_LIST based on the current_question_id.
    '''

    return "dummy question", -1
    # Sample QUESTION_LIST for demonstration purposes
QUESTION_LIST = [
    {"id": 1, "question": "What is Python?"},
    {"id": 2, "question": "What is a list in Python?"},
    {"id": 3, "question": "Explain Python dictionaries."},
]

def get_next_question(current_question_id):
    for index, question in enumerate(QUESTION_LIST):
        if question['id'] == current_question_id:
            # Check if there's a next question
            if index + 1 < len(QUESTION_LIST):
                next_question = QUESTION_LIST[index + 1]
                return next_question['question'], next_question['id']
            else:
                return "No more questions available", -1
    
    # If current_question_id is not found
    return "Question ID not found", -1

# Example usage
current_question_id = 1
next_question, next_question_id = get_next_question(current_question_id)
print(next_question, next_question_id)


def generate_final_response(session):
    '''
    Creates a final result message including a score based on the answers
    by the user for questions in the PYTHON_QUESTION_LIST.
    '''

    return "dummy result"
    # Sample QUESTION_LIST for demonstration purposes
QUESTION_LIST = [
    {"id": 1, "question": "What is Python?"},
    {"id": 2, "question": "What is a list in Python?"},
    {"id": 3, "question": "Explain Python dictionaries."},
]

def get_next_question(current_question_id):
    for index, question in enumerate(QUESTION_LIST):
        if question['id'] == current_question_id:
            # Check if there's a next question
            if index + 1 < len(QUESTION_LIST):
                next_question = QUESTION_LIST[index + 1]
                return next_question['question'], next_question['id']
            else:
                return "No more questions available", -1
    
    # If current_question_id is not found
    return "Question ID not found", -1

# Example usage
current_question_id = 1
next_question, next_question_id = get_next_question(current_question_id)
print(next_question, next_question_id)
