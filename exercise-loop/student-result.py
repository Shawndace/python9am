counter = 1
num = int(input("Enter number of student: "))

while counter <= num:
    if counter == 1:
        print("Enter eng marks: ")
        eng = int(input())
        counter += 1
    elif counter == 2:
        print("Enter math marks")
        math = int(input())
        counter += 1
    elif counter == 3:
        print("Enter sci marks")
        sci = int(input())
        counter += 1
        break
counter += 1
