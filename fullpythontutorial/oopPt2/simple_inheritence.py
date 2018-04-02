class Animal:
    cool = True

    def make_sound(self, sound):
        print("This animal says {}".format(sound))

class Cat(Animal):
    pass

a = Animal()
a.make_sound("roar")
c = Cat()
c.make_sound("meow")
# print(c.cool)

print(isinstance(c, Animal))
print(isinstance(c, Cat))
print(isinstance(c, object))
