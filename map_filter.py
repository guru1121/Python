marks =[90, 70, 75, 40, 50]


def grade(mark):
    if mark >= 90:
        return 'A'
    elif 80 <= mark < 90:
        return 'B'
    elif 50 <= mark < 80:
        return 'C'
    else:
        return 'F'

grades = map(grade, marks)

print(list(grades))
# print( "grades" ,next(grades))
# print( "grades" ,next(grades))



def FailingScore(score):
    return score < 60

result = filter(FailingScore, marks)

print("Failing Score:" ,list(result))
    
