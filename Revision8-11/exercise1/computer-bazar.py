print("----- Computer Bazaar -----")
print("Please select a device you want to purchase: ")
print("1. Dell - 2000 2. Toshiba - 3000 3. MAC - 5000")

device_cost = 0
laptop_cost = 0
del_charge = 0
pack_cost = 0
vat = 0

device = int(input("Please select a device: "))
qt = int(input("Enter quantity: "))

if device == 1:
    device_cost += 2000
    laptop_cost += device_cost * qt

elif device == 2:
    device_cost = 3000
    laptop_cost = device_cost * qt
elif device == 3:
    device_cost = 5000
    laptop_cost = device_cost * qt
else:
    print("Invalid option,try again!")
    exit()
print("--------------------")

print("Select delivery option:\n1. Yes(Rs.100)\n2. No.")
deliv = input("Please select delivery option")
if deliv == 1:
    del_charge += 100

print("--------------------")

pck = int(input("Please select packing options:"
                "\n1.Plastic 500\n2.Bag 1000\n3.Gift\n4.None\n Please enter packing option"))
if pck == 1:
    pack_cost += 500
elif pck == 2:
    pack_cost += 1000
elif pck == 3:
    pack_cost += 1500
elif pck == 4:
    pack_cost += 0
else:
    print("Invalid option")
    exit()
print("-------------------")

place = int(input("Please select place for sale!"
                  "\n1.KTM-13%VAT\n2.LAL-Free\n3.BKT-Free\n Please enter location option: "))

if place == 1:
    vat += device_cost * 0.13

grand_total = device_cost + del_charge + pack_cost + vat

print("------VOUCHER-------")

print(f"Total cost of laptop: {device_cost}")
print(f"delivery charge: {del_charge}")
print(f"packing cost: {pack_cost}")
print(f"vat included: {vat}")
print(f"Grand total: {grand_total}")

