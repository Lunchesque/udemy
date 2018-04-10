import unittest
from activities import eat, nap, is_funny, laugh

class ActivityClass(unittest.TestCase):
    def test_eat_healthy(self):
        """eat should have a positive message for healthy eating"""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, because my body is a tample"
        )
    def test_eat_unhealthy(self):
        """eat should have a YOLO message for healthy eating """
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO"
        )
    def test_eat_healthy_boolean(self):
        """is_healthy must be bool"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares")

    def test_short_nap(self):
        """short nap shold be refreshing"""
        self.assertEqual(
            nap(1),
            "I'm felleng refreshed after 1 hour nap"
        )
    def test_long_nap(self):
        """long nap should be discourgaing"""
        self.assertEqual(
            nap(3),
            "I'm overslept. I did not want to sleep for 3 hours"
        )
    def test_is_funny_tim(self):
        self.assertEqual(is_funny("tim"), False)
        # self.assertFalse(is_funny("tim"), "tim should bot bw funny")

    def test_is_funny_anyone_elese(self):
        """anyone else but tim should be funny"""
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")

    def test_laugh(self):
        self.assertIn(laugh(), ("lol", "haha", "tehehe"))

if __name__ == "__main__":
    unittest.main()
