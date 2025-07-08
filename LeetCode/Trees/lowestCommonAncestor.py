"""
Problem: 235. Lowest Common Ancestor of a Binary Search Tree
Date Completed: 7/8/2025
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Base Case
        if not root:
            return None
        # If both p and q and less than root search for LCA in left subtree of root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # If both p and q and greater than root search for LCA in right subtree of root
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If p and q are not both greater than or less than the root, the root is the LCA
        else:
            return root
