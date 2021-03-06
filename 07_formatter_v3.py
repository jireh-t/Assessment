"""Component 5 - statement formatter v3
Carry out testing
"""


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main Routine
print(formatter("-", "Welcome to the Maori numbers quiz"))
print()
print(formatter("^", "Your score was {}"))
print()
print(formatter("+", "Round {}"))
print()
print(formatter("*", "Goodbye"))




