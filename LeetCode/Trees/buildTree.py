"""
Problem: 105. Construct Binary Tree from Preorder and Inorder Traversal
Date Completed: 7/10/2025

Notes:
- Code based on NeetCode's solution
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # If the lists dont exist then the tree doesnt exist
        if not preorder or not inorder:
            return None
        # Set root to the 1st element of preorder, because that is always the root
        root = TreeNode(preorder[0])
        # Index of root in inorder array, so we know where left and right subtrees are
        mid = inorder.index(preorder[0])
        # Create left subtree, inorder: everything left of root, preorder: sublist of length the number of vals left of root
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # Create right subtree, inorder: everything right of root, preorder: sublist of length the number of vals right of root
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
