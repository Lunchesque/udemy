import jsonpickle

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# c = Cat("blue", "fold")

# with open("cat.json", "w") as file:
#     j = jsonpickle.encode(c)
#     file.write(j)

with open("cat.json", "r") as file:
    contents = file.read()
    rej = jsonpickle.decode(contents)
    print(rej)
