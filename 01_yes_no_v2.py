"""Maori quiz Yes/No
Simplifies the input by converting it to lower case. Also accepts y or n as
abbreviations. Prints result of user choice as well as input - for testing
"""

# Ask the user if they have taken the quiz before
done_before = input("Have you taken this quiz before? ").lower()

# If they say yes, output 'Program Continues'
if done_before == "y" or done_before == "yes":
    print("Program continues")

# If they say no, output 'Display Instructions'
elif done_before == "n" or done_before == "no":
    print("Instructions below")

# Otherwise - show error
else:
    print("Please answer 'y' or 'n'")

print(f"You entered '{done_before}'")

