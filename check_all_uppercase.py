#Ask user for input.
ask_user = input("Enter a word in upper cases: ")

#Check if the input is all in upper cases.
all_upper_cases = True
for character in ask_user:
    if 'a' <= character <= 'z':  
        all_upper_cases = False
        break

#Print the result whether it's true or false.