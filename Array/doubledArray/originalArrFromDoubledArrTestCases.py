import unittest
import originalArrFromDoubledArr

class OriginalArrayFromDoubledArrayTestCases(unittest.TestCase):

    def test1(self):
        changed = [1,3,4,2,6,8]
        expected = [[1,3,4], [1,4,3], [3,4,1], [3,1,4], [4,3,1], [4,1,3]]
        self.assertIn(originalArrFromDoubledArr.findOriginalArray(changed), expected)
    
    def test2(self):
        changed = [6,3,0,1]
        expected = []
        self.assertEqual(originalArrFromDoubledArr.findOriginalArray(changed), expected)
        
    def test3(self):
        changed = [1]
        expected = []
        self.assertEqual(originalArrFromDoubledArr.findOriginalArray(changed), expected)

if __name__ == '__main__':
    unittest.main()
