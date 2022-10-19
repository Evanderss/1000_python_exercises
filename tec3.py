name = input("What is your name? ")
correct_ans = int(input("How many questions did you answer correctly? "))
incorrect_ans = int(input("How many questions did you fail? "))
blank = 20 - correct_ans - incorrect_ans
    #We can also ask to user for the blank answers but this automatic in order to save time
score = (correct_ans * 5) - (incorrect_ans *2) - (blank * 1)
    #You do not need to put () but I put it in order to show me the process operation 
print(f"Welcome {name} your score was {score}")