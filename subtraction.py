import random


num1 = random.randint(0,9)

num2 = random.randint(0,9)
if num1 < num2:
    temp = num1
    num1 = num2
    num2 = temp

answer = int(input('What is %d - %d: ' %(num1,num2)))

if answer == num1 - num2:
    print('Correct')
else :
    print('Incorrect')
