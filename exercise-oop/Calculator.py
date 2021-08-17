# class Calculator:
#     # x = 10
#
#     def add(self, a, b):
#         return a + b
#
#     def sub(self, a, b):
#         return a - b
#
#     def div(self, a, b):
#         return a / b
#
#     def mul(self, a, b):
#         return a * b
#
# calc = Calculator()
# print(calc.add(10, 10))
# print(calc.sub(10,10))
# print(calc.div(10, 10))
# print(calc.mul(10, 10))
#

# ------------------SIMPLE INTREST------------
#
# class Calculator:
#
#     def take_value(self):
#         p = int(input("enter principal: "))
#         t = int(input("Enter time: "))
#         r = int(input("enter rate: "))
#         return [p, t, r]
#
#     def calculate(self):
#         obj = self.take_value()
#         x = obj[0]
#         y = obj[1]
#         z = obj[2]
#         return x * y * z / 100
#     def display(self):
#         print(self.calculate())
#
# obj2 = Calculator()
# obj2.display()