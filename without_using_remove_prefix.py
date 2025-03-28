#Ask user for input and for a prefix.
ask_user = input("Enter a word: ")
add_prefix = input("Enter the prefix that you want to remove: ")

#Remove the prefix from the input.
if ask_user .startswith(add_prefix):
    ask_user = ask_user[len(add_prefix):] 
#Print the new output. 
print("The output without the prefix is:", ask_user)