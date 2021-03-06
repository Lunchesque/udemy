class User:

    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return "{} have left the chat".format(self.first)

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def initials(self):
        return "{}.{}".format(self.first[0], self.last[0])

    def likes(self, thing):
        return "{} likes {}".format(self.first, thing)

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        return "you are now {}. happy birthday".format(self.age + 1)

print(User.active_users)

user1 = User("Perry", "Cox", 67)
user2 = User("Joe", "Tribiani", 24)
print(User.active_users)
print(user2.logout())
print(User.active_users)
# print(user2.full_name())
# print(user1.initials())
# print(user1.likes("BANANA"))
# print(user1.is_senior())
# print(user2.is_senior())
# print(user2.birthday())
