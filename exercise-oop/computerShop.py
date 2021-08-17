class computerShop:
    qt = 0
    total = 0
    delivery_charge = 0
    packing_charge = 0
    vat = 0

    def deviceOptions(self):
        print("--- Computer Shop ---")
        print("Select any option: ")
        print("1. Dell - 20,000 2. Toshiba - 30,000 3. MAC - 50,000 ")
        option1 = int(input(""))
        if option1 == 1:
            self.qt += int(input("Enter quantity: "))
            self.total += 20000 * self.qt
        elif option1 == 2:
            self.qt += int(input("Enter quantity: "))
            self.total += 30000 * self.qt
        elif option1 == 3:
            self.qt += int(input("Enter quantity: "))
            self.total += 50000 * self.qt
        else:
            print("select proper options")
            exit()

    def optionDelivery(self):
        print("--- Delivery Option ---")
        print("Enter delivery option: ")
        print("1.Home delivery-100\n2.Pickup - Free")

        deliveryOption = int(input(""))
        if deliveryOption == 1:
            self.delivery_charge = 100

    def packingOption(self):
        print("--- Packing Options ---")
        print("Enter packing options: ")
        print("1. Plastic 500\n2. Bag 1000\n3. Gift 1500\n4. None")

        packingOption = int(input(""))
        if packingOption == 1:
            self.packingCharge = 500
        elif packingOption == 2:
            self.packingCharge = 1000
        elif packingOption == 3:
            self.packingCharge = 1500
        elif packingOption == 4:
            self.packingCharge = 0
        else:
            print("select proper option!")
            exit()

    def placeOption(self):
        print("--- Delivery Place ---")
        print("1. KTM-13%VAT 2. LAL-Free 3. BKT-FREE")
        optionPlace = int(input(""))

        if optionPlace == 1:
            self.vat = self.total * 0.13


    def invoice(self):
        self.deviceOptions()
        self.packingOption()
        self.optionDelivery()
        self.placeOption()
        grand_total = self.vat + self.packing_charge + self.delivery_charge + self.total

        print("------VOUCHER-------")

        print(f"Total cost of laptop: {self.total}")
        print(f"delivery charge: {self.delivery_charge}")
        print(f"packing cost: {self.packing_charge}")
        print(f"vat included: {self.vat}")
        print(f"Grand total: {grand_total}")


obj = computerShop()
obj.invoice()


