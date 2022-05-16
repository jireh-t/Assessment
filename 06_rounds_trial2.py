"""Trial 2 for Component 4
Will not be further developed"""

import random

global rounds_played
rounds_played = 0

def quiz():

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

    # Number of rounds will go up in count
    count = 0

    # Score counter
    score = 0
    rounds_played += 1

    # Tell user what round it is
    print(f"Round {rounds_played}")
    print()

    for question in questions:
        # Loop to make the question repeat 4 times for testing
        user_answer = input(question[0]).lower()
        # Check if answer is correct by finding its place on the list
        if user_answer == (question[1]):
            print("Correct")
            print()
            score += 1
        else:
            print("Wrong")
            print(f"The answer was {question[1]}")
            print()

            # Count will go up as the user moves through the questions and
        # eventually finish the quiz
            count += 1

    # Give user score
    print(f"Your score was {score}/10")

    # Give user feedback
    if score < 6:
        print("You might need to do some more studying")

    elif score > 5 and score < 10:
        print("Great work!")

    else:
        print("Wow amazing job!!")

    print()
    play_again = input("Do you want to play another round\n<enter> to play"
                       " again or 'X' to exit").lower()
    print()

    if play_again == "x":
        print("Thanks for playing")
        print(f"You played {rounds_played} rounds")
        print("Goodbye!")

    else:
        quiz()

# Main Routine

quiz()
