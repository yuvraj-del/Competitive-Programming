"""
Problem: 98. Validate Binary Search Tree
Date Completed: 7/9/2025

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to see if a node is in the valid range
        def range(node: Optional[TreeNode], minVal: int, maxVal: int) -> bool:
            # If node doesn't exist it's in the valid range
            if not node:
                return True
            # If node if outside range return False
            if node.val <= minVal or node.val >= maxVal:
                return False
            # Recursively check each child's val for being inside range
            return range(node.left, minVal, node.val) and range(node.right, node.val, maxVal)
        return range(root, float("-inf"), float("inf"))
