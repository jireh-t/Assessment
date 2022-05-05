"""Yes/No Checking Function
based on 01_yes_no_v3
"""


# Functions go here
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


# Main Routine go here
show_instructions = yes_no("Have you taken this quiz before? ")
print(f"You entered '{show_instructions}'")
print()


