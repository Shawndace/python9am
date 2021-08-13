def simpleIntrest():
    p = int(input("enter principal: "))
    t = int(input("Enter time: "))
    r = int(input("enter rate: "))
    si = (p * t * r) / 100
    print(f"Simple intrest is: {si}")

simpleIntrest()