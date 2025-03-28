#Asks user for the specific inputs.
user_input = input("Enter a word: ")
width = int(input("Enter the total width: "))
#Calculate the padding or extra spaces to create a centered string.
padding = max(0, width - len(user_input))
padded_result = " " * (padding // 2) + user_input + " " * (padding - padding // 2)
#Print out the result.
print("The result is:", repr(padded_result))