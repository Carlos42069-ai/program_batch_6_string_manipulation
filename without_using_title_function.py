#Ask the user for a complete sentence.
user_input = input("Enter a sentence: ")
#Creating the first letter of each word capital without using title().
title_case_result = " ".join(word.capitalize() for word in user_input.split())
#Print out the result. 