import jsonpickle
from string import digits
from random import choice
from random import uniform

class Data:
    def __init__(self):
        pass

    def location_name(self):
        return "Auto_test_loc_" + "".join(choice(digits) for i in range(5))

    def location_latitude(self):
        return uniform(53.84, 53.97)

    def location_longitude(self):
        return uniform(27.42000, 27.68)

    def locations_url(self):
        return "https://172.20.9.134/s7/locations"

    def auth(self):
        return ("999", "admADM1/")
