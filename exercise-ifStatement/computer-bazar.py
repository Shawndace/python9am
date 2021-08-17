print("--- COMPUTER BAZAR ---")
print("Please select any option: ")
print("1.Dell - 20000\n2.Toshiba - 40000\n3.MAC - 50000")

optionDevice = int(input(""))
if optionDevice == 1:
    quantity = int(input("Enter quantity: "))
    total = quantity * 20000
elif optionDevice == 2:
    quantity = int(input("Enter quantity: "))
    total = quantity * 40000
elif optionDevice == 3:
    quantity = int(input("Enter quantity: "))
    total = quantity * 50000
else:
    print("Select proper option! ")
    exit()
print("--- Delivery Option ---")
print("Enter delivery option: ")
print("1.Home delivery-100\n2.Pickup - Free")

deliveryOption = int(input(""))
if deliveryOption == 1:
    delivery_charge = 100

print("--- Packing Options ---")
print("Enter packing options: ")
print("1. Plastic 500\n2. Bag 1000\n3. Gift 1500\n4. None")

packingOption = int(input(""))
if packingOption == 1:
    packingCharge = 500
elif packingOption == 2:
    packingCharge = 1000
elif packingOption == 3:
    packingCharge = 1500
elif packingOption ==4:
    packingCharge = 0
else:
    print("select proper option!")
    exit()

print("--- Delivery Place ---")
print("1. KTM-13%VAT 2. LAL-Free 3. BKT-FREE")
optionPlace = int(input(""))

if optionPlace == 1:
    vat = total * 0.13

grand_total = vat + packingCharge + delivery_charge + total

print(grand_total)

print("------VOUCHER-------")

print(f"Total cost of laptop: {total}")
print(f"delivery charge: {delivery_charge}")
print(f"packing cost: {packingCharge}")
print(f"vat included: {vat}")
print(f"Grand total: {grand_total}")





