print("--Please choose the given options to purchase--")
print("1. Dell 20000  2. Toshiba - 30000  3. MAC 50000")

dell = 20000
toshiba = 30000
mac = 50000
qt = 0
total = 0
del_charge = 0
pack_cost = 0
vat = 0

option1 = int(input("Please select a device: "))

if option1 == 1:
    qt = int(input("Enter quantity: "))
    total = qt * dell
elif option1 == 2:
    qt = int(input("Enter quantity: "))
    total = qt * toshiba
elif option1 == 3:
    qt = int(input("enter quantity"))
    total = qt * mac
else:
    print("Select valid option !! ")
    exit()
print("---------------------")

print("Please select delivery if you wish !")
print("1. Yes(rs100)\n2. No")

option2 = int(input("Please select delivery option: "))
if option2 == 1:
    del_charge = 100

print("---------------------")

print("Please select packing options!")
print("1. Plastic 500\n2. Bag 1000\n3. Gift 1500\n4. None")
option3 = int(input("Please enter packing options: "))

if option3 == 1:
    pack_cost = 500
elif option3 == 2:
    pack_cost = 1000
elif option3 == 3:
    pack_cost = 1500
elif option3 == 4:
    pack_cost = 0
else:
    print("Invalid option")
    exit()
print("-------------------")

print("Please select place for sale !")
print("1. KTM-13%VAT 2. LAL-Free 3. BKT-FREE")
option4 = int(input("Please enter location option: "))

if option4 == 1:
    vat += total * 0.13

grand_total = total + del_charge + pack_cost + vat

print("------VOUCHER-------")

print(f"Total cost of laptop: {total}")
print(f"delivery charge: {del_charge}")
print(f"packing cost: {pack_cost}")
print(f"vat included: {vat}")
print(f"Grand total: {grand_total}")
