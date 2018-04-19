import pytest
import jsonpickle
from data.loc_data_gen import location_data_generation
from fixcture.locations import Locations
from random import uniform

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        location_data_generation()
        with open("location_data.json") as file:
            content = file.read()
            d = jsonpickle.decode(content)

        fixture = Locations(d["_url"], (d["log"], d["pass"]) , d["_name"],
                            d["_latitude"], d["_longitude"])

    return fixture

@pytest.fixture(autouse = True)
def stop(request):
    def fin():
        fixture = None
    request.addfinalizer(fin)
    return fixture
