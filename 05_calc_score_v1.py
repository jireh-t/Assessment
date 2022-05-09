"""Added to 04_check_answer_v3
Added a score counter to calculate and tell the user's score at the end"""

import random

# Questions for quiz

questions = [["Maori word for 1: ", "tahi"],
             ["Maori word for 2: ", "rua"],
             ["Maori word for 3: ", "toru"],
             ["Maori word for 4: ", "wha"],
             ["Maori word for 5: ", "rima"],
             ["Maori word for 6: ", "ono"],
             ["Maori word for 7: ", "whitu"],
             ["Maori word for 8: ", "waru"],
             ["Maori word for 9: ", "iwa"],
             ["Maori word for 10: ", "tekau"]]

random.shuffle(questions)

count = 0
for question in questions:
    # User will be able to answer the question
    user_answer = input(question[0]).lower()
    # Check if answer is correct by finding its place on the list
    if user_answer == (question[1]):
        print("Correct")
    else:
        print("Wrong")

    print(f"You entered {user_answer}")

    # Count will go up as the user moves through the questions
    count += 1

