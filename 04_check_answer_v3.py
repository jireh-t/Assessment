"""Based on 04_check_answer_v2
Making the code randomly select the questions, so that it is in a different
order every time. Also convert the 2 lists into just one to make the code
more concise"""

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
    # Loop to make the question repeat 4 times for testing
        user_answer = input(question[0]).lower()
        # Check if answer is correct by finding its place on the list
        if user_answer == (question[1]):
            print("Correct")
            print()
        else:
            print("Wrong")
            print(f"The answer was {question[1]}")
            print()

        # Count will go up as the user moves through the questions and
    # eventually finish the quiz
        count += 1



