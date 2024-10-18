

 
total = 0
count = 0
while count < 10 :
    
    grade = int(input("Enter a grade: "))

    total += grade
    
    count += 1
    
average = total / count

print("The total is %d and average is %.2f" %(total,average))
