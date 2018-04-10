import unittest
from robot import Robot

class RobotTests(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot("Mega Man", batterry=50)

    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.batterry, 100)

    def test_say_name(self):
        self.assertEqual(
                self.mega_man.say_name(),
                "BEEP BOOP BEEP BOOP. I AM {}".format(self.mega_man.name.upper()))
        self.assertEqual(self.mega_man.batterry, 49)

if __name__ == "__main__":
    unittest.main()
