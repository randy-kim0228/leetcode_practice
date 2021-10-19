import unittest
import arrayOfDoubledPairs

class ArrayOfDoulbedPairsTestCases(unittest.TestCase):

    def test1(self):
        arr = [3,1,3,6]
        self.assertFalse(arrayOfDoubledPairs.canReorderDoubled(arr))
    
    def test2(self):
        arr = [2,1,2,6]
        self.assertFalse(arrayOfDoubledPairs.canReorderDoubled(arr))
        
    def test3(self):
        arr = [4,-2,2,-4]
        self.assertTrue(arrayOfDoubledPairs.canReorderDoubled(arr))

    def test4(self):
        arr = [1,2,4,16,8,4]
        self.assertFalse(arrayOfDoubledPairs.canReorderDoubled(arr))

if __name__ == '__main__':
    unittest.main()
