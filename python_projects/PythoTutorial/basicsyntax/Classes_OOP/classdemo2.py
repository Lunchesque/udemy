"""
Object Oriented Programming
"""

class Car(object):

    def __init__(self, make, model="550i"):
        self.make = make
        self.model = model

c1 = Car('bmw')
print(c1.make)
print(c1.model)

c2 = Car('benz')
print(c2.make)
print(c2.model)

print("*"*20)

class Human(object):

     def __init__(self, gender, nationality):
        self.gender = gender
        self.nationality = nationality

human1 = Human("male", "UK")
human2 = Human("male", "US")
human3 = Human("female", "ESP")

print(human1.gender)
print(human2.nationality)
print(human3.nationality, human3.gender)