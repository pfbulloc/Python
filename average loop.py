



grade = float(input('Enter a grade, enter -1 to exit: '))

total = 0
count = 0
while grade != -1 :
    
    total += grade
    count += 1
    
    grade = float(input('Enter a grade, enter -1 to exit: '))

average = total / count
print('Total is %.1f and average is %.2f' %(total, average))
    
