class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

root = TreeNode('F')
root.left = TreeNode('B')
root.right = TreeNode('G')
root.left.left = TreeNode('A')
root.left.right = TreeNode('D')
root.right.right = TreeNode('I')
root.left.right.left = TreeNode('C')
root.left.right.right = TreeNode('E')
root.right.right.left = TreeNode('H')
