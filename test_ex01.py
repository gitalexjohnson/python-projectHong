import unittest

from add_function import add
"""
def add(a, b):
    return a + b
"""
class TestAddFunction(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(1, 2), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -3)

if __name__ == '__main__':
    unittest.main()
