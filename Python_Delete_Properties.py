
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name)

try:
    print(p1.age)
except AttributeError:
    print("Error: Age property has been deleted.")