import sys
userInput = ''
count = 0

while True:
    while userInput != str(count):
        print('Whatever you do don\'t press %s!' % (count + 1))
        userInput = input()
        count += 1
        if count == 10:
            print('Wow you\'re pretty patient. Fine. You win.')
            input()
            break
        
    if userInput == str(count):
        print('I told you not to press that!')
        input()
        break
    break
sys.exit