import pytest

@pytest.fixture()
def setUp():
    print("Running conftest demo setUp")
    yield
    print("Running conftest demo tearDown")


@pytest.fixture(scope="module")
def oneTimeSetUp():
    print("Running conftest demo oneTimeSetUp")
    yield
    print("Running conftest demo oneTimeTearDown")
