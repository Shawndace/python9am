nep = float(input("Enter marks of Nepali: "))
if nep > 100:
    print("Marks is more than 100")
    exit()

eng = float(input("Enter marks of English: "))
if eng > 100:
    print("Marks is more than 100")
    exit()

mat = float(input("Enter marks of math: "))
if mat > 100:
    print("Marks is more than 100")
    exit()
sci = float(input("enter marks of science: "))
if sci > 100:
    print("Marks is more than 100")
    exit()
pop = float(input("Enter marks of population: "))
if pop > 100:
    print("Marks is more than 100")
    exit()

total = nep + eng + mat + sci + pop
perc = total / 5
division = ""

if perc > 35 and perc < 45:
    division += "Third"
elif perc > 45 and perc < 60:
    division += "second"
elif perc > 60 and perc < 75:
    division += "first"
elif perc > 75 and perc < 100:
    division += "distinction"

print("=============================")


# HOW TO VALID MARKS?

# total = nep + eng + mat + sci + pop
# perc = (total / 5)
#
# print(f"Total marks obtained is: {total}")
# print(f"Percentage: {perc} %")
#
# if perc > 35 and perc < 45:
#     print("Third division")
# elif perc > 45 and perc < 60:
#     print("second div")
# elif perc>60 and perc<75:
#     print("first div")
# elif perc>75 and perc<100:
#     print("Distiction")
# else:
#     print("Fail")
