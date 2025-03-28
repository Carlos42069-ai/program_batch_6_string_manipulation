#Ask user for input.
user_input = input("Enter a word: ")
#Converting the first letter inputed into a capital and all other letters in lower case.
if user_input:
    capitalized_result = user_input[0].upper() + user_input[1:].lower()

#Print out the results.
print("Capitalized string:", capitalized_result)