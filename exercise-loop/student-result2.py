num = int(input("Enter number of students: "))
increment = 1
student_mark = []

while increment <= num:
    print(f"----Student {increment}----")
    for marks in range(1):
        nep = float(input("Enter nepali marks: "))
        eng = float(input("Enter english marks: "))
        collected_marks = [nep, eng]
        student_mark.append(collected_marks)
    increment += 1

student = []
# student_mark = [[2,3],[3,4]]
for s_mark in student_mark:
    total_mark = 0
    for tot in s_mark:
        total_mark += tot
    student.append(total_mark)

x= 1
for tots in student:
    perc = tots / 5
    divison = ""

    if perc > 35 and perc < 45:
        divison += 'third'
    elif perc > 45 and perc < 60:
        divison += 'second'
    elif perc > 60 and perc < 75:
        divison += 'first'
    elif perc > 75 and perc < 100:
        divison += 'distinction'
    else:
        divison += 'pass'

    print(f"-------Student result of {x}-----------")
    print(f"Total: {tots} percentage: {perc} Divison: {divison}")
    x += 1