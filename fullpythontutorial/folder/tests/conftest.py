import pytest
from driver.driver import Driver

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Driver(headers={"Accept": "application/json"},
                        verify=False)
    return fixture

@pytest.fixture(autouse = True)
def stop(request):
    def fin():
        fixture = None
    request.addfinalizer(fin)
    return fixture
