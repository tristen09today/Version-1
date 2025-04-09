#This following program is a simple and basic version for my quiz
age_str=str()
score = 0
#Questions and answers as a tuple   
questions = [
    ("What is the capital of England? :[London, Paris, Rome, Madrid]", "london"),
    ("Which built-in function can get information from the user [input, question, parameter]", "input"),
    ("Which keyword do you use to loop over a given list of elements", "for")
]
#Ask the users to input their name using a
while True:
    name = input('What is your name:')
    if name == "":
        print('Please enter your name in the field')
        continue
    #if the name is a numerical it will print a statement
    elif name.isdigit():
        print('Please use the alphabets')
        continue
    else:
        break
#Ask the users to input their age
while True:
    age_str=input('How old are you :')
    if age_str == (""):
        print('Please enter your age in the field')
        continue
    #If age is a digit and is within the age bracket it will continue otherwise it will print not eligible
    elif age_str.isdigit():
        age = age_str(int)
        if 13<=age<=17:
            break
        else:
            print('You are not eligible to play')
            continue
    else:
        print('You must enter in numbers')
        continue


#Ask if the users would like to read the rules
while True:
    rules = input(f'Hello {name}, would you like to read the rules?[Yes/No] \n')
    #if the user enters yes, display rules. 
    if rules.lower()=='yes':
        print('************RULES************ \n')
        print('1. Answer all the questions \n')
        print('2. Do not get any help \n')
        print('3. Do your personal best and have fun!\n')
        print('*****************************\n')
        break
    #If the user inputs no, breeak out of the whileloop
    elif rules.lower() =='no':
        break
    else:
        print('Please enter Yes or No')
        continue
#Prints the questions and adds to score
while True:
    #Uses a for loop to print out the questions
    for question, correct_answer in questions:
        answer = input(f'{question}\nOut of the options what is the answer?\n :')
        #If the answer is linked to the user's input print "correct" else print "incorrect" and display the correct answer
        if answer.lower() == correct_answer:
            print("Correct!\n")
            score=score+1      
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}\n")
    break
            
#prints the score out of the total number of questions       
print(f"You got a score of {score} out of {len(questions)} questions correct!\n")
quit()

