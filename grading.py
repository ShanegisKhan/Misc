import sys

def getScore(): # Get score from user
    score = input('Enter your score (or type "exit" to quit\n')
    return score

def isValidNumber(number): # checks to see if score input is a valid number 1-100
    if number.isdigit() and int(number) in range(1, 101):
        return True

def getGrade(score): # gets grade from score 
    if score in range(1, 50):
        grade = 'F'
    elif score in range(50, 70):
        grade = 'D'
    elif score in range(70, 80):
        grade = 'C'
    elif score in range(80, 90):
        grade = 'B'
    elif score in range(90, 101):
        grade = 'A'
    else:
        grade = 'invalid'
    return grade
        
def checkIfAn(grade): # checks to see if a or an should be used
    if grade == 'F' or grade == 'A':
        an = 'n'
    else:
        an = ''
    return an

while True: # main loop
    score = getScore()
    if score == 'exit':
        break
    elif isValidNumber(score):
        grade = getGrade(int(score))
        n = checkIfAn(grade)
        print('You got a%s %s' % (n, grade))
        
sys.exit()