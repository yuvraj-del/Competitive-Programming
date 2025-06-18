"""
Problem: 226. Invert Binary Tree
Date Completed: 6/18/2025
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If the tree is empty return None
        if not root:
            return None
        # Swap the left and right
        root.left, root.right = root.right, root.left
        # Recursively invert the children
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root
