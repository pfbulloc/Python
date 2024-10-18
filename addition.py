import random



loop = 0

correctCount = 0

while loop < 10 :
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    answer = int(input('What is %d + %d: ' %(num1,num2)))

    if num1 + num2 == answer:
        correctCount += 1
       
    loop += 1

print('You got %d questions correct' % correctCount)
