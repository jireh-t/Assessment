"""Maori Quiz base component
Components added after they have been created and tested
"""


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


# Main Routine go here
played_before = yes_no("Have you taken this quiz before? ")

if played_before == "No":
    instructions()

else:
    print("Program continues")

