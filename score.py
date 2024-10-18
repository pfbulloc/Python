
score = int(input('Enter your score: '))

if score >= 0 and score <= 100:
    if score >= 90 and scrore <= 100:
        print('A')
    elif score >= 80 and score < 90:
        print('B')
    elif score >= 70 and score <80:
        print('C')
    elif score >= 60 and score <70:
        print('D')
    else :
        print('F')
else :
    print('invalid score entered')
