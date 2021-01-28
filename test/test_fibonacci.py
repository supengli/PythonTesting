import unittest
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent / "src"))

from Package import fibonacci    # The code to test

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(fibonacci(3), 2)

    def test_negative(self):
        with self.assertRaises(ValueError) as e:
            fibonacci(-1)

if __name__ == '__main__':
    unittest.main()
