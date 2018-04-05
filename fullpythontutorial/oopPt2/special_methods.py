class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    def __repr__(self):
        return "Human named {} {} aged {}".format(self.first, self.last, self.age)
    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="newborn", last=self.last, age=0)
        return "You cant add that"

    def __mul__(self, other):
        if isinstance(other, int):
            return [self for i in range(other)]
        return "cant multiply that"

j = Human("jack", "troll", 34)
k = Human("kate", "nottroll", 31)
# print(j)
# print(len(j))

print(j * 2)
