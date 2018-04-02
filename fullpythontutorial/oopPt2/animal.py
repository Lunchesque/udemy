class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return "{} is a {}".format(self.name, self.species)

    def make_sound(self, sound):
        print("This animal says {}".format(sound))

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print("{} plays with {}".format(self.name, self.toy))


blue = Cat("Blue", "Fold", "String")
blue.play()
