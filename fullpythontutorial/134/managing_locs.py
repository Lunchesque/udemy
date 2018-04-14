import requests
from random import uniform

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
    _name = input("Input name of location: ")
    latitude = uniform(53.84, 53.97)
    longitude = uniform(27.42000, 27.68)
    payload = {"name": _name,
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

def get_location_id(_name_for_delete):
    locations = get_locations()
    return str([location["id"] for location in locations if location["name"] == _name_for_delete][0])

def delete_location():
    locations = [location["name"] for location in get_locations()]
    print(locations)
    _name_for_delete = input("Input name location for delete: ")
    _url = "https://172.20.9.134/s7/locations/" + get_location_id(_name_for_delete)

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

managing_locations()
