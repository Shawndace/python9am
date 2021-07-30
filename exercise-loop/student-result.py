num = int(input("enter a number: "))
counter = 1
student_marks = []
while counter <= num:
    print(f"-----Student: {counter}-----")
    for marks in range(1):
        eng = float(input("Enter english marks: "))
        if eng > 100:
            print("Invalid marks")
            exit()
        nep = float(input("Enter nep marks: "))
        if nep > 100:
            print("Invalid marks")
            exit()
        marks = [eng, nep]
    student_marks.append(marks)
counter += 1

student = []

# [[1,1],[1,1]]
for each_mark in student_marks:
    total = 0
    for tot in each_mark:
        total += tot
    student.append(total)

x = 1

for result in student:
    perc = result / 5
    divison = ''

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
    print(f"Total: {result} percentage: {perc} Divison: {divison}")
    x += 1

# num = int(input("Enter number of students: "))
# counter = 1
# student_mark = []
# total_mark = 0
# student = []
# while counter <= num:
#     print(f"-------student {counter}---------")
#     for mark in range(1):
#         eng = float(input("Enter english marks: "))
#         nep = float(input("Enter nepali marks: "))
#         marks = [eng, nep]
#         student_mark.append(marks)
#
#     counter += 1
#
# for s_mark in student_mark:
#     total_mark = 0
#     for tot in s_mark:
#         total_mark += tot
#     student.append(total_mark)
# x = 1
# for sk in student:
#     perc = sk / 5
#     divison = ''
#
#     if perc > 35 and perc < 45:
#         divison += 'third'
#     elif perc > 45 and perc < 60:
#         divison += 'second'
#     elif perc>60 and perc<75:
#         divison += 'first'
#     elif perc>75 and perc<100:
#         divison += 'distinction'
#     else:
#         divison += 'pass'
# print("-----Student Result---------")
# print(f"tota: {sk} Percentage: {perc} Division: {divison} ")
# x += 1
