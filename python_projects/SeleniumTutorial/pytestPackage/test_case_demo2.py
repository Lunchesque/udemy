import pytest

@pytest.fixture()
def setUp():
    print("Running demo2 setUp")
    yield
    print("Running demo2 tearDown")

def test_methodA(setUp):
    print("Running demo2 method A")

def test_methodB(setUp):
    print("Running demo2 method B")
