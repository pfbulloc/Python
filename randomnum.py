import random
num1 = random.randint(0,9)

num2 = random.randint(0,9)
answer = int(input('What is %d + %d: ' %(num1,num2)))

if num1 + num2 == answer:
    print('Correct')
else :
    print('Incorrect')
