#This following program is Version 3 of my quiz, in which imports easygui
from easygui import*
import matplotlib.pyplot as plt

import random
# Initializing variables
title = "User information"
msg = "WELCOME TO QUIZ!"
MIN_AGE = 13
MAX_AGE = 18
MIN_YEAR_LEVEL = 9
MAX_YEAR_LEVEL = 13

field_name = ["Name", "Last Name", "Year Level", "Age"]
#General Quiz(list of tuples)
#Some multiple choice questions with the correct answer
gen_questions = [
    #Some multiple choice questions with the correct answer
    #The questions are in the form of a tuple, with the first element being the question and the second element being the correct answer
    ("(0) What is the capital of New Zealand? \n (A) Auckland\n (B) Wellington\n (C) Christchurch\n (D) Hamilton", "B"),
    ("(1) What is the capital of England? \n (A) London\n (B) Paris\n (C) Rome\n (D) Madrid ", "A"),
    ("(2) What is the capital of Australia?\n (A) Sydney\n (B) Melbourne\n (C) Canberra\n (D) Brisbane ", "C"),
    ("(3) Which planet is known as the Red Planet?\n (A) Earth\n (B) Mars\n (C) Jupiter\n (D) Venus", "B"),
    ("(4) Which country has won the most FIFA World Cup titles?\n (A) Germany\n (B) England\n (C) Argentina\n (D) Brazil", "D"),
    ("(5) What element is found on Mars giving its red colour?\n (A) Copper\n(B) Titanium\n(C) Iron\n(D) Magnesium", "C"),
]
#Math Quiz
mat_questions = [
    ("(1) What is the value of 7x8?\n (A) 54\n (B) 56\n (C) 58\n (D) 60", "B"),
    ("(2) Solve for x in the equation: 2x+5=13\n (A) 2\n (B) 3\n (C) 4\n (D) 5", "C"),
    ("(3) If a = 3 and b=4, what is 3a+4b?\n (A) 25\n (B) 18\n (C) 32\n (D) 27", "A"),
    ("(4) What is 15 x 4? \n (A)60\n (B) 50\n (C) 75\n (D) 45", "A"),
    ("(5) Simplify the expression: 4(3x+2)-2(x-5)?\n (A) 14x+18\n (B) 14x-18\n (C) 14x+15\n (D) 10x+18", "D"),
]
#Science Quiz
sci_questions = [
    ("(1) What is the speed of light?\n (A) 300000km/s\n (B) 75000km/s\n (C) 450000km/s\n (D) 150000km/s", "A"),
    ("(2) Calculate the work done on an object that has a mass of 1kg and travels a distance of 100m?\n (A) 1000J\n (B) 10J\n (C) 100J\n (D) 10000J", "A"),
    ("(3) What is the chemical formula for Potassium Chloride?\n (A) KC \n (B) PCl\n (C) PoC\n (D) KCl", "D"),
    ("(4) Which scientist is known for the theory of general relativity \n (A) Nikola Tesla\n  (B) Isaac Newton \n (C) Albert Einstein\n (D) Christopher Luxon", "B"),
    ("(5) What is DNA?\n (A) Deoxyribonucleic Acid\n (B) Deoxyribonucleic Alkaline\n (C) Deoxymanal Acid", "A"),
]
#FUNCTION TO SEE IF USER IS ELIGIBLE TO DO QUIZ
# FUNCTION TO SEE IF USER IS ELIGIBLE TO DO QUIZ
def eligibility(age, year_level):
    # Constants
    

    if MIN_AGE <= age <= MAX_AGE and MIN_YEAR_LEVEL <= year_level <= MAX_YEAR_LEVEL:
        return True
    else:
        return False


#TAKES THE QUIZ_TYPE AND LINKS IT TO THE FUNCTION PARAMETER (questions) in which prints the quiz questions and answers. 
def run_quiz(questions,quiz_type):
    score = 0
    random.shuffle(questions)#Shuffle the questions for randomness
    for question, correct_ans in questions:
        #Displays question with options and a quit button 
        answer = buttonbox(f'{question}\nOut of the options what is the answer?', choices=['A', 'B', 'C', 'D', 'QUIT'])
        if answer == 'QUIT':
            msgbox(f"You got a score of {score} out of {len(questions)} questions correct!\n")
            return
        elif answer in ['A', 'B', 'C', 'D']:
            if answer == correct_ans:
                score += 1
                msgbox(f"Correct! (Your Current Score is {score})")
                
            else:
                #If the user were to input a wrong answer, it will show the correct answer and display thier current score
                msgbox(f"Wrong! The correct answer is {correct_ans!r}, not {answer!r}\n(Your Current Score is {score}")
    #Ater all the questions have been displayed, it will show the final score
    msgbox(f"You got a score of {score} out of {len(questions)} questions correct!\n")
    #display a bar graph of the score and incorrect answers using matplotlib pie chart
    incorrect = len(questions) - score
    labels = ['Correct Answers', 'Incorrect Answers']
    sizes = [score, incorrect]
    colors = ['#66c2a5', '#fc8d62']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(f'{name}\'s Score in {quiz_type} Quiz')
    plt.show()
    plt.close()






    


#Where the program starts
field_value = multenterbox(msg, title, field_name) 
while field_value is not None:
    #resets the error message
    errmsg = ""
    #The code iterates over the indicies of field_name, and check if the input is empty to the field_value.
    for i in range(len(field_name)):
        #If the field_name is "", append a error message
        if field_value[i].strip() == "":
            errmsg += f'"{field_name[i]}" is a required field.\n\n'

    # If no fields are blank, check age and year level eligibility
    if errmsg == "":
        name, age, year_level = field_value[0], field_value[3], field_value[2]
        if age.isdigit() and year_level.isdigit():
            age = int(age)
            year_level = int(year_level)
            name = str(name)
            if eligibility(age, year_level):
                break# Exit the loop if eligibility criteria are met
            else:
                errmsg = "You are not eligible to play the quiz.\n\n"
        else:
            errmsg = "Age and Year Level must be numeric.\n\n"

    # Show the multenterbox again with the error message if any
    field_value = multenterbox(errmsg, title, field_name, field_value)

    # Exit if the user presses cancel
    if field_value is None:
        quit()
#Display the rules using an external file
while True:
    rules = buttonbox(f'{name} Would you like to read the rules? [Yes/No]', choices=['Yes', 'No', 'Quit'])
    if rules == 'Yes':
        with open("rules.txt", "r") as f:
            data = f.read()
            msgbox(data)
            break
    elif rules == 'Quit':
        quit()
    elif rules == 'No':
        break
    else:
        msgbox('Please select Yes or No')
        continue
#Selects quiz_topic


 

while True:
    try:
        #Ask the users to choose a quiz_type 
        quiz_topic = buttonbox('Which quiz would you like to do?\n A) General Knowledge\n B) Math\n C) Science', choices=['A', 'B', 'C','Quit'])
        if quiz_topic == "A":
            #Runs the function for questions, by linking the quiz_type parameter to questions in the function above.
            run_quiz(gen_questions,"general_Quiz") #Run General knowledge quiz
        elif quiz_topic == "B":
            run_quiz(mat_questions,"math") #Run Math quiz 
        elif quiz_topic == "C":
            run_quiz(sci_questions,"science") #Run Science quiz
        elif quiz_topic =="Quit":
            quit()
        else:
            msgbox('Please use A, B, or C')
            continue
        #After all the questions have been answered,the program will ask the user to either do more quiz or quit the program 
        restart_quiz = buttonbox('Do you wish to do more quizes? [Yes or No]', choices=['Yes', 'No'])
        if restart_quiz.lower() == 'yes':
            continue
        elif restart_quiz.lower() == 'no':
            quit()
        break
    except ValueError:
        msgbox('Something has occurred')
