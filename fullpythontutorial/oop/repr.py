class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return "There are currently {} active users".format(cls.active_users)

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return "{} is {}".format(self.first, self.age)

    def logout(self):
        User.active_users -= 1
        return "{} have left the chat".format(self.first)

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def initials(self):
        return "{}.{}.".format(self.first[0], self.last[0])

    def likes(self, thing):
        return "{} likes {}".format(self.first, thing)

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        return "{} is now {}. happy birthday!".format(self.first, self.age + 1)

tom = User.from_string("Tom,Jones,89")
j = User("judy", "steele", 18)
print(j)
j = str(j)
print(j)
