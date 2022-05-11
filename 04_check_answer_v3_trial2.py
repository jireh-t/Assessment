"""Based on 04_check_answer_v2
Trialing a different way to randomly generate questions"""

import random

# Number of rounds
count = 0
while count != 10:

# Computer will choose a number and that number will correspond to a question
    number = random.randint(1, 10)

    if number == 1:
        answer = input("Maori word for 1: ").lower()
        # Check if answer is correct
        if answer == "tahi":
            print("Correct")
        else:
            print("Wrong")
            print(f"The answer was tahi")
        print()

        count += 1

    elif number == 2:
        answer = input("Maori word for 2: ").lower()
        # Check if answer is correct
        if answer == "rua":
            print("Correct")
        else:
            print("Wrong")
            print(f"The answer was rua")
        print()

        count += 1

    elif number == 3:
        answer = input("Maori word for 3: ").lower()
        # Check if answer is correct
        if answer == "toru":
            print("Correct")
        else:
            print("Wrong")
            print(f"The answer was toru")
        print()

        count += 1

    elif number == 4:
        answer = input("Maori word for 4: ").lower()
        # Check if answer is correct
        if answer == "wha":
            print("Correct")
        else:
            print("Wrong")
            print(f"The answer was wha")
        print()

        count += 1

    elif number == 5:
        answer = input("Maori word for 5: ").lower()
        # Check if answer is correct
        if answer == "rima":
            print("Correct")
        else:
            print("Wrong")
            print(f"The answer was rima")
        print()

        count += 1

    elif number == 6:
        answer = input("Maori word for 6: ").lower()
        # Check if answer is correct
        if answer == "ono":
            print("Correct")
        else:
            print("Wrong")
            print(f"The answer was ono")
        print()

        count += 1

    elif number == 7:
        answer = input("Maori word for 7: ").lower()
        # Check if answer is correct
        if answer == "whitu":
            print("Correct")
        else:
            print("Wrong")
            print(f"The answer was whitu")
        print()

        count += 1

    elif number == 8:
        answer = input("Maori word for 8: ").lower()
        # Check if answer is correct
        if answer == "waru":
            print("Correct")
        else:
            print("Wrong")
            print(f"The answer was waru")
        print()

        count += 1

    elif number == 9:
        answer = input("Maori word for 9: ").lower()
        # Check if answer is correct
        if answer == "iwa":
            print("Correct")
        else:
            print("Wrong")
            print(f"The answer was iwa")
        print()

        count += 1

    elif number == 10:
        answer = input("Maori word for 10: ").lower()
        # Check if answer is correct
        if answer == "tekau":
            print("Correct")
        else:
            print("Wrong")
            print(f"The answer was tekau")
        print()

        count += 1

