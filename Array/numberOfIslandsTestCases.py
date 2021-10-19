import unittest
import numberOfIslands

class NumberOfIslandsTestCases(unittest.TestCase):

    def test1(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ]
        expected = 1
        self.assertEqual(numberOfIslands.numIslands(grid), expected)
    
    def test(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ]
        expected = 3
        self.assertEqual(numberOfIslands.numIslands(grid), expected)

if __name__ == '__main__':
    unittest.main()
