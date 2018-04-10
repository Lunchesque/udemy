class Robot:
    def __init__(self, name, batterry=100, skills=[]):
        self.name = name
        self.batterry = batterry
        self.skills = skills

    def charge(self):
        self.batterry = 100
        return self

    def say_name(self):
        if self.batterry > 0:
            self.batterry -= 1
            return("BEEP BOOP BEEP BOOP. I AM {}".format(self.name.upper()))
        return "Low power. Recharge the batterry and try again"

    def learn_skills(self, new_skill, cost_to_learn):
        if self.batterry >= cost_to_learn:
            self.batterry -= cost_to_learn
            self.skills.append(new_skill)
            return "WOAH. I KNOW {}".format(new_skill.upper())
        return "Insufficient batterry. Recharge the batterry and try again"
