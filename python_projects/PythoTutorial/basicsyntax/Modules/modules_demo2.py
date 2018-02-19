from modulesexternal.car import info

class ModulesDemo2():

    def car_description(self):
        make = "BMW"
        model = "550i"
        info(make, model)


m = ModulesDemo2()
m.car_description()