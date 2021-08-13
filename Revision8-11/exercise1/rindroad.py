print("$$$ RING ROAD BUS FARE $$$")
print("1. Kalanki to chabahil \n 2. Chabahil to kalanki")
route = int(input("Please enter a route option: "))

charge = 0

if route == 1:
    charge += 30
    print(f"charge is: {charge}")
elif route == 2:
    charge += 60
    print(f"charge is: {charge}")
else:
    print("Invalid route! ")