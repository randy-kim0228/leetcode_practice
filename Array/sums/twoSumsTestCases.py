import unittest
import twoSums

class TwoSumsTestCases(unittest.TestCase):

    def test1(self):
        nums = [2,7,11,15]; target = 9
        expected = [0,1]
        self.assertEqual(twoSums.twoSums(nums, target), expected)
    
    def test2(self):
        nums = [3,2,4]; target = 6
        expected = [1,2]
        self.assertEqual(twoSums.twoSums(nums, target), expected)
    
    def test3(self):
        nums = [3,3]; target = 6
        expected = [0, 1]
        self.assertEqual(twoSums.twoSums(nums, target), expected)

if __name__ == '__main__':
    unittest.main()
