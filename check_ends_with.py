#Ask the user for input and suffix to check if the word ends with the given suffix.
ask_user = input("Enter a word with a suffix: ")
suffix_input = input("Enter a suffix to check: ")
#Check if the suffix inputed is within the given word.
check_suffix = ask_user[-len(suffix_input):] == suffix_input if len(suffix_input) <= len(ask_user) else False

#Print if it is true or false.