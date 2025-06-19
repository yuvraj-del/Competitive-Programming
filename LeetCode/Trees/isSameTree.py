"""
Problem: 100. Same Tree
Date Completed: 6/19/2025
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None the trees match
        if not p and not q:
            return True
        # If both nodes exist
        if p and q:
            # Left, right and current values must match
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # If only one node is None trees differ
        else:
            return False
