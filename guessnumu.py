import random
maxnum = int(input("Enter max number"))
num = random.randint(1, maxnum)
print(num)
guessnum = int(input('Guess the random number (1 and max included): ')

if guessnum == num:
    print('Congrats! you guessed it')
else :
    print('Sorry, incorrect')
