import jsonpickle
from string import digits
from random import choice
from random import uniform


def location_data_generation():
    _name = "Auto_test_loc_" + "".join(choice(digits) for i in range(5))
    _latitude = uniform(53.84, 53.97)
    _longitude = uniform(27.42000, 27.68)
    data = {"_url": "https://172.20.9.134/s7/locations",
            "log": "999",
            "pass": "admADM1/",
            "_name": _name,
            "_latitude": _latitude,
            "_longitude": _longitude
            }
    with open("location_data.json", "w") as file:
        d = jsonpickle.encode(data)
        file.write(d)

    print(data["pass"])

def get_location_data():
    location_data_generation()
    with open("location_data.json") as file:
        content = file.read()
        d = jsonpickle.decode(content)
    return d

location_data_generation()
