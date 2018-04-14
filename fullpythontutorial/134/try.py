import requests

def get_locs():
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
print(get_locs())
