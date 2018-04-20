import requests
import jsonpickle
from random import uniform

class Locations:

    def __init__(self, _url, _auth, _name, _latitude, _longitude):
        self._url = _url
        self._auth = _auth
        self._name = _name
        self._latitude = _latitude
        self._longitude = _longitude

    def get_locations(self):
        response = requests.get(self._url,
            headers={"Accept": "application/json"},
            verify=False,
            auth=self._auth,
            params={"limit": "15",
            "offset": "0",
            "order_by": "name"}
        )
        locations = response.json()
        return locations

    def add_location(self):
        payload = {"name": self._name,
                    "latitude": self._latitude,
                    "longitude": self._longitude,
                    "cameras": [],
                    "localserver_id": 2}

        res = requests.post(self._url,
            headers={"Accept": "application/json"},
            verify=False,
            auth=self._auth,
            data=payload
        )

    def rename_location(self):
        locations = self.get_locations()
        loc_id = [location["id"] for location in self.get_locations() if "Auto_test_loc" in location["name"]]
        _url = "{}/{}".format(self._url, str(loc_id[0]))
        payload = {"name": "new",
                    "cameras": [],
                    "localserver_id": 2,
                    "id": loc_id
                    }
        res = requests.put(_url,
                            headers={"Accept": "application/json"},
                            verify=False,
                            auth=self._auth,
                            data=payload
                            )
        print(loc_id)
        print(_url)
        print(res)

    def delete_location(self):
        loc_id = [location["id"] for location in self.get_locations() if "Auto_test_loc" in location["name"]]
        _del_url = "{}/{}".format(self._url, str(loc_id[0]))
        deletion = requests.delete(_del_url,
            headers={"Accept": "application/json"},
            verify = False,
            auth=self._auth
            )
        print(loc_id)
        print(_del_url)
        print(deletion)
