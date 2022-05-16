"""Maori Quiz base component
Components added after they have been created and tested
"""
import random

# yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'
        if answer == "y" or answer == "yes":
            answer = "Yes"
            return answer

        # If they say no, output 'Display Instructions'
        elif answer == "n" or answer == "no":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer with 'yes' or 'no'")


# Function to display instructions
def instructions():
    print("*** How to Play ***")
    print()
    print("The rules of the game will go here")
    print()
    print("Program continues")
    print()


# Quiz function
def quiz():

    rounds_played = 0

    play_again = ""
    while play_again != "x":

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

        # Tell user what round it is
        rounds_played += 1
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

        # Ask user if they want to play again
        print()
        play_again = input("Do you want to play another round\n<enter> to play"
                           " again or 'X' to exit").lower()
        print()

    # Goodbye message
    print("Thanks for playing")
    print(f"You played {rounds_played} round(s)")
    print("Goodbye!")


# Main Routine
print("Welcome to the numbers Maori quiz")
print()
played_before = yes_no("Have you taken this quiz before? ")
print()

if played_before == "No":
    instructions()

else:
    print("Program continues")

quiz()
