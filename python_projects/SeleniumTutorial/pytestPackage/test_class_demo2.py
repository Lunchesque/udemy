"""
if not using autouse we have to provide fixture classSetup in all methods in the test class like a parameter
autouse=True --> every method of this class will know about "classSetup" fixture and automaticly use this fixture
without providing this fixture in every method (imagine if have 100 test methods in this class...)
"""


import pytest
from SeleniumTutorial.pytestPackage.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.abc = SomeClassToTest(self.value)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("The result is -> " + str(result))

    def test_methodB(self):
        print("Running method B")
