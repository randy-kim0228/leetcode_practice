
import unittest
import preorder
import inorder
import postorder
from TreeNode import root

class TreeTraversalTestCase(unittest.TestCase):
    
    def test_preorder(self):
        print('Testing Pre-Order Traversal (Recursively & Iteratively).')
        self.assertEqual(preorder.recursively(root), preorder.expected_result)
        self.assertEqual(preorder.iteratively(root), preorder.expected_result)

    def test_inorder(self):
        print('Testing In-Order Traversal (Recursively & Iteratively).')
        self.assertEqual(inorder.recursively(root), inorder.expected_result)
        self.assertEqual(inorder.iteratively(root), inorder.expected_result)
    
    def test_postorder(self):
        print('Testing Post-Order Traversal (Recursively & Iteratively).')
        self.assertEqual(postorder.recursively(root), postorder.expected_result)
        self.assertEqual(postorder.iteratively(root), postorder.expected_result)

if __name__ == '__main__':
    unittest.main()