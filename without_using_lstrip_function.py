#Ask user for input
ask_user = input("Enter a word with spaces in the beginning: ")

#Code that removes the spaces without using the lstrip function.
space = 0

while space < len(ask_user) and ask_user[space] == ' ':
    space += 1

#print the output.
print("The output now is:", (ask_user[space:]))