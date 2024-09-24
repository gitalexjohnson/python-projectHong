import unittest
from List01 import add_value, sort_value, delete_value  # Replace 'your_module' with the actual module name

class TestListFunctions(unittest.TestCase):

    def test_add_value(self):
        test_list = []
        result = add_value(test_list, 'Python')
        self.assertEqual(result, ['Python'])
        self.assertEqual(test_list, ['Python'])  # Ensure the original list is modified

    def test_sort_value(self):
        test_list = ['C', 'A', 'B']
        result = sort_value(test_list)
        self.assertEqual(result, ['A', 'B', 'C'])

    def test_delete_value(self):
        test_list = ['Python', 'Java', 'C++']
        result = delete_value(test_list, 'Java')
        self.assertEqual(result, ['Python', 'C++'])

    def test_delete_value_non_existent(self):
        test_list = ['Python', 'Java', 'C++']
        with self.assertRaises(ValueError):
            delete_value(test_list, 'Ruby')  # Ruby is not in the list

if __name__ == '__main__':
    unittest.main()
