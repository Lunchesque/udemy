"""
File name should start with test
test method name should start with test

pytest test_mod.py -> run tests in module
pytest somePath    -> run all tests below somePath
pytest test_module.py:: test_method -> only rur test_method in test_module

-s key -> to print statements
-v key -> verbose
"""

import pytest

@pytest.fixture()
def setUp():
    print("Running demo3 setUp")
    yield
    print("Running demo3 tearDown")

def test_demo3_methodA(setUp):
    print("Running demo3 method A")

def test_demo3_methodB(setUp):
    print("Running demo3 method B")
