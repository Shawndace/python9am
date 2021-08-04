# function scope-GLobal and local:
# x = 10

# global

# def test():
#     global x
#     x += 30
#     print(x)
#
# test()
#-----------------------------
# def test():
#     """
#     This is test funtion
#
#     """
#     return "Hello"
# print(test)
# print(test())
# print(test.__doc__)
# print(test.__name__)
# ------------------------------
# def my_name():
#     def my_friend():
#         return "Sophia"
#     return my_friend()
#
# print(my_name())
# --------------------------------
# annonomous function
# x = lambda a, b : a + b
# print(x(2,3))

# import calculate
# print(calculate.add(4, 5))

# * all
# from calculate import add as sum
# print(sum(2, 3))
# print(sum(5, 2))

# from lib import demo
# print(demo.test())
# from lib.demo import test
from lib import *
print(demo.test())
print(intro.get())