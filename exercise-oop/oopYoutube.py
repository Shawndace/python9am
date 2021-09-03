class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        return self.age

d = Dog("Tim", 4)
d.set_age(6)
print(d.get_age())
# print(f"{d.name} is {d.age} years")
# print(d.get_name())
# print(d.get_age())
