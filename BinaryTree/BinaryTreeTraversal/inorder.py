"""
Inorder traversal:
    1) Visit left subtree
    2) Visit root
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

inorder result = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
"""
from TreeNode import root

def recursively(root):
    # using depth first search
    res = []
    def dfs(root):
        if root:
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
    dfs(root)
    return res

def iteratively(root):
    # using stack
    res = []
    stack = []
    while root or stack:
        while root: # visit most left first, in the mean time, append roots to the stack
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res

expected_result = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

if __name__ == '__main__':
    recursive_output = recursively(root)
    iterative_output = iteratively(root)
    assert recursive_output == expected_result
    assert iterative_output == expected_result
