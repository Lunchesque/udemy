import pytest


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser, osType):

    print("Running conftest demo oneTimeSetUp")
    if browser == "firefox":
        value = 10
        print("Running test on FF")
    else:
        value = 20
        print("Running test on Chrome")

    if request.cls is not None:
        request.cls.value = value

    yield value
    print("Running conftest demo oneTimeTearDown")

@pytest.fixture()
def setUp():
    print("Running conftest demo setUp")
    yield
    print("Running conftest demo tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="type of OS")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
