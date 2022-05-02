# Ask the user if they have taken the quiz before
done_before = input("Have you taken this quiz before? (y/n) ")

# If they say yes, output 'Program Continues'
if done_before == "y":
    print("Program continues")

# If they say no, output 'Display Instructions'
elif done_before == "n":
    print("Instructions below")

# Otherwise - show error
else:
    print("Please answer 'y' or 'n'")
