import requests
from data.data import Data

class Driver(Data):
    def __init__(self, headers, verify):
        self.headers = headers
        self.verify = verify

    def get_locations(self):
        response = requests.get(self.locations_url(),
            headers=self.headers,
            verify=self.verify,
            auth=self.auth(),
            params={"limit": "15",
            "offset": "0",
            "order_by": "name"}
        )
        # print(response.text)
        locations = response.json()
        return locations

    def add_location(self):
        payload = {"name": self.location_name(),
                    "latitude": self.location_latitude(),
                    "longitude": self.location_longitude(),
                    "cameras": [],
                    "localserver_id": 2}

        res = requests.post(self.locations_url(),
            headers=self.headers,
            verify=self.verify,
            auth=self.auth(),
            data=payload
        )

    def rename_location(self):
        locations = self.get_locations()
        loc_id = [location["id"] for location in self.get_locations() if "Auto_test_loc" in location["name"]]
        loc_name = str([location["name"] for location in self.get_locations() if "Auto_test_loc" in location["name"]][0])
        _url = "{}/{}".format(self.locations_url(), str(loc_id[0]))
        payload = {"name": loc_name + "_renamed",
                    "cameras": [],
                    "localserver_id": 2,
                    "id": loc_id
                    }
        res = requests.put(_url,
                            headers=self.headers,
                            verify=self.verify,
                            auth=self.auth(),
                            data=payload
                            )
        print(loc_id)
        print(_url)
        print(res)

    def delete_location(self):
        loc_id = [location["id"] for location in self.get_locations() if "Auto_test_loc" in location["name"]]
        _del_url = "{}/{}".format(self.locations_url(), str(loc_id[0]))
        deletion = requests.delete(_del_url,
            headers=self.headers,
            verify=self.verify,
            auth=self.auth()
            )
        print(loc_id)
        print(_del_url)
        print(deletion)
