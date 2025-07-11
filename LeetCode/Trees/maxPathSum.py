"""
Problem: 124. Binary Tree Maximum Path Sum
Date Completed: 7/11/2025

Notes:
- Solution inspired by NeetCode
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize a instance ans var
        self.ans = float("-inf")
        # Helper function to calculate max gain from current node down
        def maxDepth(node: Optional[TreeNode]) -> int:
            # Base case
            if not node:
                return 0
            # Recursively find max value of subtrees
            # max(subtree, 0): to cut out all negative paths
            left = max(maxDepth(node.left), 0)
            right = max(maxDepth(node.right), 0)
            # Store current max path sum
            self.ans = max(self.ans, node.val + left + right)
            # Return max value so far
            return node.val + max(left, right)
        maxDepth(root)
        return self.ans
