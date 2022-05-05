"""Maori quiz Yes/No
Puts the code created in v2 into a loop to make testing easier and more
efficient.
"""

done_before = ""
while done_before != "x":

    # Ask the user if they have played before
    done_before = input("Have you taken this quiz before? ").lower()

    # If they say yes, output 'Program Continues'
    if done_before == "y" or done_before == "yes":
        print("Program continues")

    # If they say no, output 'Display Instructions'
    elif done_before == "n" or done_before == "no":
        print("Instructions below")

    # Otherwise - show error
    else:
        print("Please answer with 'yes' or 'no'")

    print(f"You entered '{done_before}'")


