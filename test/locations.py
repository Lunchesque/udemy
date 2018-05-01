import requests
from random import uniform
from random import choice
from string import digits

class Locations:

    def __init__(self, name):
        self.name = name

    def get_locations():
        _locs_url = "https://172.20.9.134/s7/locations"
        response = requests.get(
            _locs_url,
            headers={"Accept": "application/json"},
            verify=False,
            auth=("999", "admADM1/"),
            params={"limit": "15",
            "offset": "0",
            "order_by": "name"}
        )
        locations = response.json()
        return locations


    def add_location():
        _url = "https://172.20.9.134/s7/locations"
        loc_id = ''.join(choice(digits) for i in range(5))
        name = "Auto_test_loc_" + loc_id
        latitude = uniform(53.84, 53.97)
        longitude = uniform(27.42000, 27.68)
        payload = {"name": name,
                    "latitude": latitude,
                    "longitude": longitude,
                    "cameras": [],
                    "localserver_id": 2}
        res = requests.post(
            _url,
            headers = {"Accept": "application/json"},
            verify = False,
            auth = ("999", "admADM1/"),
            data=payload
        )

    def get_location_id():
        locations = get_locations()
        return str([location["id"] for location in locations if "Auto_test_loc_" in location["name"]])

    def delete_location():
        _url = "https://172.20.9.134/s7/locations/" + get_location_id()

        deletion = requests.delete(_url,
                        headers = {"Accept": "application/json"},
                        verify = False,
                        auth = ("999", "admADM1/")
                        )
        print(deletion)
        print(_url)

    def managing_locations():
        action = input("What do you want to do with locations (add/del): ")
        if action == "add":
            add_location()
        elif action == "del":
            delete_location()
        else:
            print("Provide a correct action")
