# class Mobile:
#
#     def brand(self):
#         return "mobile"
#
# class Samsung(Mobile):
#     pass
#
# obj = Samsung()
# print(obj.brand())

class Mobile:
    # x = 10
    def __init__(self):
        print("This is constructor!")

class Phone(Mobile):
    def __init__(self):
        super().__init__()
        # Mobile.__init__(self)

obj = Phone()
# obj.Brand()
# print(obj.x)