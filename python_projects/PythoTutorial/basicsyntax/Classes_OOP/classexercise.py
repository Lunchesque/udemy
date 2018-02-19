
class Fruit(object):

    def __init__(self):
        print("This is a fruit")

    def nutrition(self):
        print("Fruit is nutrition")

    def fruit_shape(self):
        print("This is a shape")


class Apple(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("Tjis is an apple")

    def nutrition(self):
        print("Child nutrition")

    def color(self):
        print("Apple is RED")

f = Fruit()
f.fruit_shape()
f.nutrition()

print("*"*20)

a1 = Apple()
a1.fruit_shape()
a1.nutrition()
a1.color()


