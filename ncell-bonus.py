minute = int(input("enter minutes a user talked: "))

if minute >= 1 and minute <= 100:
    if minute >= 1 and minute <= 10:
        print("5m bonus")
    if minute >= 10 and minute <= 20:
        print("10m bonus")
    if minute >= 20 and minute <= 40:
        print("15m bonus")
    if minute >=40 and minute>=60:
        print("You got 50m bonus!!")
    if minute >=60 and minute <=100:
        print("Congratulations you got 100m bonus")
else:
    print("Not bonus")
