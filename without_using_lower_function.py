#Ask user for an input.
ask_user = input("Enter a word: ")
#Code that lowers the characters without using lower().
lowercase_output = ""
for character in ask_user:
    if 'A' <= character <= 'Z':
        lowercase_output += chr(ord(character) + 32)
    else:
        lowercase_output += character


#Print the output.
print("The lowercase output is:", lowercase_output)