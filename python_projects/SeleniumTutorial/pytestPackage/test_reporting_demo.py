"""
To generate HTML report of the test results use "--html=filename.html" commandline key to
generate report in the project folder itself (eg: --html=filename.html)
To generate HTML report of the test results in the specific path
use the "--html=path/filename.html" commandline key (eg: --html=/home/"username"/REPORT.html)
"""

import pytest
from SeleniumTutorial.pytestPackage.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestReportingDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        result = self.abc.sumNumbers(2, 8)
        assert result > 20
        print("Running method B")
