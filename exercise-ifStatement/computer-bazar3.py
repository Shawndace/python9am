
device_cost = 0
deliver_cost = 0
pack_cost = 0
vat = 0


opt1 = int(input("please select a device: 1. Dell - 20000 2. Toshiba - 30000 3. MAC - 50000 "))
if opt1 == 1:
    qty = int(input("enter quantity: "))
    device_cost = qty * 20000
elif opt1 == 2:
    qty = int(input("enter quantity: "))
    device_cost = qty * 30000
elif opt1 == 3:
    qty = int(input("enter quantity: "))
    device_cost = qty * 50000
else:
    print("Select valid number")
    exit()

print("-----------------------")

opt2 = int(input("Enter deliver option: 1. Yes(100) 2.No"))
if opt2 == 1:
    deliver_cost += 100
elif opt2 == 2:
    deliver_cost += 0
else:
    exit()

opt3 = int(input("Select packing option: 1. Plastic 500 2. Bag 1000 3.Gift 1500 4. None"))
if opt3 == 1:
    pack_cost += 500
elif opt3 == 2:
    pack_cost += 1000
elif opt3 == 3:
    pack_cost += 1500
elif opt3 == 4:
    pack_cost += 0
else:
    exit()

opt4 = int(input("Enter place to sale: 1. KTM-13%VAT 2. LAL-Free 3. BKT-FREE "))
if opt4 == 1:
    vat += 0.13 * device_cost
elif opt4 == 2:
    vat += 0
elif opt4 == 3:
    vat += 0
else:
    exit()

grand_total = device_cost + deliver_cost + pack_cost


print("------Voucher----------")
print(f"Laptop cost:{device_cost}")
print(f"delivery charge: {deliver_cost}")
print(f"packing cost: {pack_cost}")
print(f"VAT: {vat}")
print(f"grand total: {grand_total}")