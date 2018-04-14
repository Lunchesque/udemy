import requests
import jsonpickle

url = "https://172.20.9.134/s7/events/search-with-data?count=36&include_total_count=true&location_id=311&order_type=desc&since=2018-04-12T21:00:00.000Z&until=2018-04-13T21:00:00.000Z"


# def get_events():
#     response = requests.post(
#         url,
#         headers={"Accept": "application/json"},
#         verify=False,
#         auth = ("999", "admADM1/"),
#         params={"events": "0"}
#     ).json()
#     return [event["alarm"] for event in response["events"] if event["topic"] == "FaceInList"]
# print(get_events())


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
    return locations[0]["name"]
print(get_locs())
