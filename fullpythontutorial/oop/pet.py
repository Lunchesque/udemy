class Pet:
    allowed = ["cat", "dog", "fish", "rat"]
    def __init__(self, name, species):
        if species not in self.allowed:
            raise ValueError("You cant have this species pet")
        self.name = name
        self.species = species

    def set_species(self,species):
        if species not in self.allowed:
            raise ValueError("You cant have this species pet")
        self.species = species

    def a_pet(self, name, species):
        return "You have {} named {}".format(self.species, self.name)

cat = Pet("Blue", "cat")
dog = Pet("Rex", "dog")
print(cat.a_pet("Blue", "cat"))
print(dog.a_pet("Rex", "dog"))
