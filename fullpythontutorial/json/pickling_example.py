import pickle

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return "{} is {}".format(self.name, self.species)

    def make_sound(self, sound):
        print("this animal says {}".format(sound))

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print("{} plays with {}".format(self.name, self.toy))
#
# blue = Cat("Blue", "Fold", "String")
#
# with open("pets.pickle", "wb") as file:
#     pickle.dump(blue, file)

with open("pets.pickle", "rb") as file:
    new_blue = pickle.load(file)
    print(new_blue)
    print(new_blue.play())
