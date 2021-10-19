"""
The height of a tree -> the number of edges on the longest path from the root to the leaf (a leaf node has a height of 0).
The height of a tree <=> the depth of its deepest node.

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the ** NUMBER OF NODES ** along the longest path from the root node down to the farthest leaf node.

Ex.         3
           / \
          9  20
            /  \
           15   7


"""

def maxDepth(root):
    # recursion, bottom-up approach; at leaf, the height is 0
    def dfs(root):
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        return 1 + max(left, right)
    return dfs(root)
