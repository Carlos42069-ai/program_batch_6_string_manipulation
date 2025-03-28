#Ask the user for inputs.
user_input = input("Enter a word: ")
width = int(input("Enter the total width: "))

#Adding space that completes the given number in the function parameter.
padded_result = user_input + " " * (width - len(user_input)) if len(user_input) < width else user_input

#Print out the result.

