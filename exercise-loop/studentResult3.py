num = int(input("enter number of students: "))
increment = 1
student_mark = []

while increment <= num:
    print(f"Student {increment}")
    for marks in range(1):
        nep = int(input("enter nepali marks: "))
        eng = int(input("enter english marks: "))
        marks_collected = [nep, eng]
        student_mark.append(marks_collected)
    increment += 1

# print(student_mark)

student = []
for inside in student_mark:
    total_mark = 0
    for tot_marks in inside:
        total_mark += tot_marks
    student.append(total_mark)

# print(student)
x = 1
for total in student:
    per = total / 2
    div = ''

    if per > 35 and per < 45:
        div += 'third'
    if per > 45 and per < 65:
        div += 'second'
    if per > 65 and per < 75:
        div += 'first'
    if per > 75 and per < 100:
        div += 'Distinction'
    else:
        div += 'Pass'

    print(f"------Student Result of {x}------")
    print(f"total: {total} Percentage: {per} divison: {div}")
    x += 1