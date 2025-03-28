#Asks user for input.
user_input = input("Enter a word: ")
#Create a code that has the same function with swapcase without using the function.
swapped_result = "".join(chr(ord(c) ^ 32) if c.isalpha() else c for c in user_input)

#Print out the results.
print("Swapped case string:", swapped_result)