import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not True")
        b = False
        self.assertFalse(b, "b is not False")

    def test_assertEqual(self):
        a = "test"
        b = "test"
        c = "test1"
        self.assertEqual(a, b, "'a' not equal 'b'")
        self.assertNotEqual(a, c, "'a' equal 'c'")

if  __name__ == "__main__":
    unittest.main(verbosity=2)