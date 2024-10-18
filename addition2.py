import random




loop = 0

correctCount = 0

num1 = random.randint(0,9)
num2 = random.randint(0,9)

answer = int(input('What is %d + %d: ' %(num1,num2)))

while answer != num1 + num2 :

    print('Incorrect Try again')

    answer = int(input('What is %d + %d: ' %(num1,num2)))

print('Correct')
