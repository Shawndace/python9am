print("==================================")
print("=======Computer Bazaar============")


dell = 20000
toshiba = 30000
mac = 50000
qt = 0
total = 0
del_charge = 0
pack_charge = 0
vat = 0

print("=======Product list===============")
print("1. Dell - 20,000 2. Toshiba - 30,000 3. MAC - 50,000 ")
option1 = int(input("Enter any option: "))

if option1 == 1:
    qt += int(input("Enter quantity: "))
    total += dell * qt
elif option1 == 2:
    qt += int(input("Enter quantity: "))
    total += toshiba * qt
elif option1 == 3:
    qt += int(input("Enter quantity: "))
    total += mac * qt
else:
    print("Enter quantity")
    exit()

print("Delivery option: ")
print("1. Home - Rs.1000 2. Pickup - Free")
option2 = int(input("Enter delivery option: "))

if option2 == 1:
    del_charge += 1000

print("Select packing options: ")
print("1. Plastic-Rs500 2. Bag-Rs1000 3.Gift Box-Rs5000 4.None")
option3 = int(input("Enter any packing options: "))

if pack_charge == 1:
    pack_charge += 500
elif pack_charge == 2:
    pack_charge += 1000
elif pack_charge == 3:
    pack_charge += 5000
else:
    pack_charge += 0

print("Select locations: ")
print("1. KTM-13% VAT 2.LTP-Free 3.Bkt-Free")
option4 = int(input("Enter location options: "))

if option4 == 1:
    vat += total * 0.13

grand_total = total + del_charge + pack_charge + vat

print("===============================")
print(f"Device: {option1}")
print(f"quantity: {qt}")
print(f"Total cost for device: {total}")
print(f"Vat amount: {vat}")
print(f"Grand total: {grand_total}")
