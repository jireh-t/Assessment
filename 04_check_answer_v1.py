"""Carrying on from 04_ask_question_v1
Adjusting it to make it check the answers"""

# Questions for quiz

questions = ["Maori word for 1: ",
             "Maori word for 2: ",
             "Maori word for 3: ",
             "Maori word for 4: ",
             "Maori word for 5: ",
             "Maori word for 6: ",
             "Maori word for 7: ",
             "Maori word for 8: ",
             "Maori word for 9: ",
             "Maori word for 10: ",]

# Corresponding answers for quiz
answers = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru",
           "iwa", "tekau"]

count = 0
for question in questions:
    # User will be able to answer the question
    user_answer = input(question)
    # Check if answer is correct by finding its place on the list
    if user_answer == (answers[count]):
        print("Correct")
    else:
        print("Wrong")
    # Count will go up as the user moves through the questions
    count += 1
