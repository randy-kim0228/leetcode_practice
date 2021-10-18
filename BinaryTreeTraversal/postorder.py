"""
Postorder traversal:
    1) Visit left subtree
    2) Visit right subtree
    3) Visit root

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

postorder result = ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']
"""
from TreeNode import root

def recursively(root):
    # using depth first search
    res = []
    def dfs(root):
        if root:
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
    dfs(root)
    return res

def iteratively(root):
    # we can utilize the preorder traversal method
    # preorder (root -> left -> right), modify it to do traverse (root -> right -> left)
    # return the reverse of the resulted modified preorder (left -> right -> root)
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return res[::-1]

expected_result = ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']

if __name__ == '__main__':
    recursive_output = recursively(root)
    iterative_output = iteratively(root)
    assert recursive_output == expected_result
    assert iterative_output == expected_result
