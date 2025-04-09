'''This program is VERSION 2 of making a quiz(Functions, Multiple Quiz type, external files and more user-friendly)
A messy and Big Program For VERSION 3. iT will be complex but simple'''
#Initializing variables
quiz1 = ()
gen_questions =[]
mat_questions =[]
sci_questions =[]
restart_quiz='yes'
#Questions and answers as a tuple
#GENERAL QUIZ QUESTIONS
gen_questions = [
    ("(1)What is the capital of England? [London, Paris, Rome, Madrid]","london"),
    ("(2)What is the capital of Australia? [Sydney, Melbourne, Canberra, Brisbane]","canberra"),
    ("(3)Which planet is known as the Red Planet? [Earth, Mars, Jupitar, Venus]","mars"),
    ("(4)Which country has won the most FIFA World Cup titles? \n [Germany, England, Argentina, Brazil]","brazil"),
    ("(5)What element is found on Mars giving its red colour? [Copper, Titanium, Iron, Magnesium]","iron"),
]
#MATH QUIZ QUESTIONS
mat_questions = [
    ("(1)What is th evalue of 7x8?\n [54,56,58,60]","56"),
    ("(2)Solve for x in the equation: 2x+5=13\n [2, 3, 4, 5]","3"),
    ("(3)If a = 3 and b=4, what is 3a+4b? [25, 18, 32, 27]","25"),
    ("(4)What is 15 x 4? \n [, 60, 50, 75]","60"),
    ("(5) simplify the expression: 4(3x+2)-2(x-5)? [14x+18, 14x-18, 14x+15, 10x+18]","10x+18"),
]
#SCIENCE QUIZ QUESTIONS
sci_questions = [
    ("(1)What is the speed of light? [300000km/s, 75000km/s, 450000km/s, 150000km/s]","300000km/s"),
    ("(2)Calculate the work done on an object that has a mass of 1kg and travels a distance of 100m?\n [1000J, 10J, 100J, 10000J]","1000J"),
    ("(3)What is the chemical formula for Potassium Chloride? [KCl, PCl, PoC, KC]","kcl"),
    ("(4)Which scientist is known for the theory of general relativity \n [Issac Newton, Nikola Tesla, Albert Einstein, Benjamin Franklin]","Issac Newton"),
    ("(5)What is DNA? [Deoxyribonucleic Acid, Deoxryibonucleic Alkaline, Deoxymanal Acid, ]","deoxyribonucleic acid"),
]

#This function checks if the user is in range of age.
def eligibility(age,year):
    if 13 <= age <= 17 and 9 <= year <= 13:
        return True
'''
Underneath displays the questions and options in which links the user's input to the answer.
If the user's input is not correct,it will print the correct answer.
Before the questions are displayed, the score is set to 0.
'''
    
#Function to run general quiz using for loop    
def quiz1(gen_questions):
    while True:
        score = 0
        for gen_question, correct_answer in gen_questions:
            answer = input(f'{gen_question}\nOut of the options what is the answer?\n :')
            if answer.lower() == correct_answer:
                print("Correct!")
                score+=1    
            else:
                print(f"The answer is {correct_answer!r}, not {answer!r}\n")      
        break
    return score
#Function to run math quiz, using for loop
def quiz2(mat_questions):
    while True:
        score = 0
        for mat_question, correct_answer in mat_questions:
            answer = input(f'{mat_question}\nOut of the options what is the answer?\n :')
            if answer == correct_answer:
                if answer is str():
                    print('Incorrect please enter a integer')
                print("Correct!")
                score+=1    
            else:
                print(f"The answer is {correct_answer!r}, not {answer!r}\n")      
        break
    return score
#Function to run science quiz, using for loop
def quiz3 (sci_questions):
    while True:
        score = 0
        for sci_question, correct_answer in sci_questions:
            answer = input(f'{sci_question}\nOut of the options what is the answer?\n :')
            if answer.lower() == correct_answer:
                print("Correct!")
                score+=1    
            else:
                print(f"The answer is {correct_answer!r}, not {answer!r}\n")      
        break
    return score
#Restarts the quiz and checks if the user has inputted a correct input
def restart(restart_quiz):
    while True:
        restart_quiz=input('Do you wish to do more quiz? [Yes or No] \n :')
        if restart_quiz.lower() =='yes':
            return True
        elif restart_quiz.lower() =='no':
            quit()
        else:
            print('Please enter yes or no')
            continue
    

#BEGINNING PROGRAM
print('WELCOME TO YOUR QUIZ!')
#Input Name and imports external text file(rules.txt) if user entrs yes
while True:
    name = input('What is your name:')
    if name == "":
        print('Please enter your name in the field')
        continue
    elif name.isdigit():
        print('Please use the alphabets')
        continue
    else:
        break
#Ask users for age and year, and runs the function "Eligibility" to check if users can play
while True:
    age_str=input('How old are you : ')
    if age_str == (""):
        print('Please enter your age in the field')
        continue
    year_str=input('Enter year level: ')
    if year_str == (""):
        print('Please enter year level')
        continue

    #Checks if age and year level are integers, if so run the eligbility function
    if age_str.isdigit() and year_str.isdigit():
        age = int(age_str)
        year = int(year_str)
        if eligibility(age,year):
            break
        else:
            print('You are not eligible to play')
            continue
    else:
        print('You must enter in numbers')
        continue
#According to the input, the user enters it will either read the rules or no.
while True:
    rules = input(f'Hello {name}, would you like to read the rules?[Yes/No] \n :')
    if rules.lower() == 'yes':
        with open("rules.txt","r") as f:
            data = f.read()
            print(data)
            break
    elif rules.lower() =='no':
        break
    else:
        print('Please select Yes or No')
        continue
#Quiz Type and SCORE            
while True:
    try:
        #Ask the user what type of quiz they would like to do
        quiz_topic = input('What quiz would you like to do \n[A)General Knowledge, B)Math, C)Science](Use A,B,C) \n:')
        #If the user chooses a, they will do the general quiz
       
        if quiz_topic.lower() == "a":
            print('GOOD LUCK!')
            score = quiz1(gen_questions)#The quiz will return the score value and tell the user what they got
            print(f"You got a score of {score} out of {len(gen_questions)} questions correct!\n")
           
            #if the user scores below 66% on the quiz, they will be given a encouraging message
            if score<=3:
                print('****DONT GIVE UP YOU CAN DO IT***')
               
        #if the user chooses b, they will do the math quiz
        elif quiz_topic.lower() == "b":
            score = quiz2(mat_questions)
            print(f"You got a score of {score} out of {len(mat_questions)} questions correct!\n")
            if score<=3:
                print('****DONT GIVE UP YOU CAN DO IT***')
        #if the user chooses C, they will do the science quiz        
        elif quiz_topic.lower() == "c":
            score = quiz3(sci_questions)
            #len is the total
            print(f"You got a score of {score} out of {len(sci_questions)} questions correct!\n")
            if score<=3:
                print('****DONT GIVE UP YOU CAN DO IT***')
        else:
            #if users were to enter a invalid case, the program will ask the user to re-enter
            print('Please try again, enter (A,B,C)')
            continue
        #Euns the function when the usuer is finished with the quiz to see if they would like to do more
        if restart(restart_quiz):
            continue
            
        
         
    except ValueError:
        print('Something has occurred')
    
        #Ask if the users would like to restart and do more quizzes
       
