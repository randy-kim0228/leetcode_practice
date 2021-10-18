
import os
import json
import unittest
import subarraySumEqualsK

with open('./Array/subarraySumEqualsK/largeTestCase.json') as json_file:
    json_data = json.load(json_file)

class subarraySumEqualsKTestCase(unittest.TestCase):
    
    def test_case1(self):
        nums = [1, 1, 1]; k = 2
        expected = 2
        self.assertEqual(subarraySumEqualsK.usePrefixTable(nums, k), expected)
        self.assertEqual(subarraySumEqualsK.useHashTable(nums, k), expected)
    
    def test_case2(self):
        nums = [1, 2, 3]; k = 3
        expected = 2
        self.assertEqual(subarraySumEqualsK.usePrefixTable(nums, k), expected)
        self.assertEqual(subarraySumEqualsK.useHashTable(nums, k), expected)

    def test_case3(self):
        nums = json_data['nums']; k = json_data['k']
        expected = 4012
        # self.assertEqual(subarraySumEqualsK.usePrefixTable(nums, k), expected)
        self.assertEqual(subarraySumEqualsK.useHashTable(nums, k), expected)


if __name__ == '__main__':
    unittest.main()