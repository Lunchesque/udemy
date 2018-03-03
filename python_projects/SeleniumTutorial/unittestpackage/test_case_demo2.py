import unittest

class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*#"*20)
        print("I will run only once before all tests")
        print("*#"*20)

    def setUp(self):
        print("I will run before every test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("I will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("*#"*20)
        print("I will run only once after all tests")
        print("*#"*20)

if __name__ == "__main__":
    unittest.main(verbosity=2)