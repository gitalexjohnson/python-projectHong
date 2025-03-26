"""
1. run unit test
2. import the library
3. access the functions in List for AT2 Part A
make some changes 
"""
"""
flowchart 
"""
import unittest # import the unittest library

from List01 import add_value, sort_value, delete_value

class TestListFunctions(unittest.TestCase):

    def test_add_value(self):
        test_list = []
        result = add_value(test_list, "Hong")
        self.assertEqual(result,['Hong2'])
        self.assertEqual(test_list, ['Hong'])

    def test_sort_value(self):
        test_list = ['Hong','Charlie', 'Alan']
        result = sort_value(test_list)
        self.assertEqual(result, ['Alan','Charlie','Hong2'])

    def test_delete_value(self):
        test_list = ['Hong','Charlie', 'Alan']
        result = delete_value(test_list, 'Hong')
        self.assertEqual(result, ['Charlie', 'Alan'])
"""
    def test_delete_not_found(self):
        test_list = ['Hong','Charlie', 'Alan']
        with self.assertRaises(ValueError):
            delete_value(test_list, 'John')
"""  
if __name__ == '__main__':
    print("I am here",__name__)
    unittest.main() 
