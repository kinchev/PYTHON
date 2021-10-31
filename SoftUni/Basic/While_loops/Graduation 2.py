name = input()
excluded = 0
counter = 0
sum_grades = 0
while True:
    grade = float(input())
    sum_grades += grade
    counter += 1
    if grade < 4:
        excluded += 1
        if excluded > 1:
            print(f"{name} has been excluded at {counter - 1} grade")
            break
    if counter == 12:
        print(f"{name} graduated. Average grade: {sum_grades / counter:.2f}")
        break
