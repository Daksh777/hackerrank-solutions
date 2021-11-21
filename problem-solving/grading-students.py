num = int(input())
grades = [int(input()) for _ in range(num)]

for grade in grades:
    if grade < 38:
        print(grade)
    else:
        print(max([grade, round(grade/5) * 5]))