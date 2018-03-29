class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

user1 = User("Perry", "Cox", 37)
user2 = User("Joe", "Tribiani", 24)

print(user1.first, user1.age)
print(user2.last, user2.first)
