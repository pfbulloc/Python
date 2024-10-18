

num = int(input("Enter a number (Enter -1 to exit): "))
even = 0
odd = 0
while num != -1 :
    if num % 2 ==  0 :
        even += num
    else :
        odd += num
    num = int(input("Enter a number: "))
print("The sum of the even numbers is %d and the sum of odd numbers is %d" %(even,odd))
