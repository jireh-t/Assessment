"""Based on 04_check_answer_v3
Make the code into a loop, to make it easier and more efficient for testing
It repeats each question 4 times, so I can carry out my tests
"""

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
    for item in range (4):
        user_answer = input(question[0]).lower()
        # Check if answer is correct by finding its place on the list
        if user_answer == (question[1]):
            print("Correct")
            print()
        else:
            print("Wrong")
            print(f"The answer was {question[1]}")
            print()

        # Count will go up as the user moves through the questions
        count += 1

