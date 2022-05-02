"""Maori quiz Yes/No
Puts the code created in v2 into a loop to make testing easier and more
efficient.
"""

played_before = ""
while played_before != "x":

    # Ask the user if they have played before
    played_before = input("Have you played this game before? ").lower()

    # If they say yes, output 'Program Continues'
    if played_before == "y" or played_before == "yes":
        print("Program continues")

    # If they say no, output 'Display Instructions'
    elif played_before == "n" or played_before == "no":
        print("Instructions below")

    # Otherwise - show error
    else:
        print("Please answer with 'yes' or 'no'")

    print(f"You entered '{played_before}'")


