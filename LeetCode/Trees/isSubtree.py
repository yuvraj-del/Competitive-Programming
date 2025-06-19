"""
Problem: 572. Subtree of Another Tree
Date Completed: 6/19/2025
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Check if two trees are same (code from sameTree.py in my repo)
        def sameTree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root and not subRoot:
                return True
            if root and subRoot:
                return root.val == subRoot.val and sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)
            else:
                return False

        # Base case
        if not root:
            return False

        # If the trees match at the current node return True
        if sameTree(root, subRoot):
            return True

        # Recursively check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
