class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return "There are currently {} active user(s)".format(cls.active_users)

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

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
        return "{}.{}.".format(self.first[0], self.last[0])

    def likes(self, thing):
        return "{} likes {}".format(self.first, thing)

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        return "{} is now {}. happy birthday!".format(self.first, self.age + 1)


class Moderator(User):
    total_mods = 0
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_active_mods(cls):
        return "There are currently {} active mod(s)".format(cls.total_mods)

    def remove_post(self):
        return "{} removed a post from {} community".format(self.full_name(), self.community)


u1 = User("Tom", "Garcia", 35)
u2 = User("Cliff", "Edwards", 47)
u3 = User("Jess", "Wachowski", 20)
mod1 = Moderator("Jass", "O'conner", 61, "Piano")
mod1 = Moderator("Jass", "O'conner", 61, "Piano")
print(User.display_active_users())
print(Moderator.display_active_mods())









#dsdsd
