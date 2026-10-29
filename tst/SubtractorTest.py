import unittest
from src.Subtractor import Subtractor

class SubtractorTest(unittest.TestCase):
    def test_subtractor(self):
        sub = Subtractor()
        self.assertEqual(sub.subtract(5,2),3)

if __name__ == "__main__":
    unittest.main()
