def student_marks():
        nep = int(input("Enter nepali marks: "))
        eng = int(input("Enter english marks: "))
        math = int(input("Enter math marks: "))
        sci = int(input("Enter sci marks: "))
        pop = int(input("Enter pop marks: "))
        return [nep, eng, math, sci, pop]


def calculate_tot():
    total = student_marks()
    a = total[0]
    b = total[1]
    c = total[2]
    d = total[3]
    e = total[4]
    plus = a + b + c + d + e
    return plus

def calculate_perc():
    perc = calculate_tot() / 5
    return perc

def calculate_div():
    perc = calculate_perc()
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

def display():
    print(calculate_tot())
    # print(calculate_perc())
    # print(calculate_div())

display()



