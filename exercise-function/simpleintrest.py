def take_value():
    p = int(input("Enter principal: "))
    t = float(input("Enter time: "))
    r = float(input("Enter rate: "))

    return [p, t, r]


def calculate():
    obj = take_value()
    x = obj[0]
    y = obj[1]
    z = obj[2]
    return x * y * z / 100


def display():
    print(calculate())

display()