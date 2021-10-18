"""
Preorder traversal:
    1) Visit root
    2) Visit left subtree
    3) Visit right subtree

Time Complexity: O(N) where N is the number of nodes
Space Complexity: O(N), skewed binary tree may take up entire tree node

Example:
                F
              /   \
            B      G
           / \      \
          A   D      I
             / \    /
            C   E  H

preorder result = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
"""
from TreeNode import root

def recursively(root):
    # using depth first search
    res = []
    def dfs(root):
        if root:
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
    dfs(root)
    return res

def iteratively(root):
    # using stack
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left) # Based on LIFO (Last In First Out)
    return res
    
expected_result = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']

if __name__ == '__main__':
    recursive_output = recursively(root)
    iterative_output = iteratively(root)
    assert recursive_output == expected_result
    assert iterative_output == expected_result
