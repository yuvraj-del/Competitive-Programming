"""
Problem: 104. Maximum Depth of Binary Tree
Date Completed: 6/19/2025
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case of recursion
        if not root:
            return 0
        # Adds 1 and takes the maximum between max depths of right and left subtrees
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
