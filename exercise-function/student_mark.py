def student_marks():
    nep = int(input("Enter nepali marks: "))
    eng = int(input("Enter english marks: "))
    return [nep, eng]

def calculate_tot():
    total = student_marks()
    a = total[0]
    b = total[1]
    sum = a + b
    return sum

def calculate_perc():
    percent = calculate_tot()/2
    return percent

# print(f"percentage: {calculate_perc()}")


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
    print(f"total is: {calculate_tot()} ")
    print(f"percentage is: {calculate_perc()}")
    # print(f"divison is: {calculate_div()}")

display()
