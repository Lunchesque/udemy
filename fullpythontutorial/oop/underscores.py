class Person:
    def __init__(self):
        self._secret = "hi"
        self.name = "Jon"
        self.__msg = "I like tirtles"
p = Person()

print(p.name)
print(p._secret)
print(p._Person__msg)
