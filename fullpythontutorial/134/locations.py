import requests

class Locations:

    def __init__(self, _locs_url, creds, params):
        self._locs_url = _locs_url
        self.creds = creds
        self.params = params

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
