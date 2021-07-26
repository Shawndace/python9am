nep = float(input("Enter marks of Nepali: "))
eng = float(input("Enter marks of English: "))
mat = float(input("Enter marks of math: "))
sci = float(input("enter marks of science: "))
pop = float(input("Enter marks of population: "))

total = nep + eng + mat + sci + pop
perc = (total / 5)

if nep < 100 or eng < 100 or mat < 100 or sci < 100 or pop < 100:
    if perc > 35 and perc < 45:
        print("Third division")
    elif perc > 45 and perc < 60:
        print("second div")
    elif perc > 60 and perc < 75:
        print("first div")
    elif perc > 75 and perc < 100:
        print("Distiction")
else:
    print("Marks is invalid")

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
