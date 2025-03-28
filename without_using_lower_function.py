#Ask user for an input.
ask_user = ("Enter a word: ")
#Code that lowers the characters without using lower().
lowercase_output = ""
for character in user_input:
    if 'A' <= character <= 'Z':
        lowercase_result += chr(ord(character) + 32)
    else:
        lowercase_result += character


#Print the output.