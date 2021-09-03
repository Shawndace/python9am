class Mobile:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # self.price = price

    def get_brand(self):
        # return self.brand
        print(f"brand is{self.brand}")
    def get_model(self):
        # return self.model
        print(f"model is: {self.model}")
    # def get_price(self):
    #     # return self.price
    #     print(f"price is: {self.price}")

class Mi(Mobile):
    def __init__(self, brand, model):
        super().__init__(brand, model)

class Samsung(Mi):
    def __init__(self, brand, model, price):
        super().__init__(brand, model)
        self.price = price

    def get_price(self):
        print(f"price is: {self.price}")

# obj = Mi('MI','6x','45000')
# obj.get_brand()
# obj.get_model()
# obj.get_price()

obj = Samsung('Samsung','4A','45000')
obj.get_model()
obj.get_price()


