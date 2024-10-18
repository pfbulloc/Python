import random
ranNum = random.randint(1,20)
print(ranNum)
guessNum = int(input("Guess the number between 1-20: "))

while guessNum != ranNum :
    if guessNum < ranNnum :
        print("Your guess is too low")
    else :
        print("Your guess is too high")
        
    guessNum = int(input("Guess the number between 1-20: "))

print('Correct')
