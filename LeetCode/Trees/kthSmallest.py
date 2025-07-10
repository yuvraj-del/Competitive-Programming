"""
Problem: 230. Kth Smallest Element in a BST
Date Completed: 7/10/2025
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Creates list of sorted vals in BST
        ans = []
        # Depth-First Search
        def dfs(node: Optional[TreeNode]) -> None:
            # Left -> Node -> Right (increasing order)
            # If node.left exists dfs on left child
            if node.left:
                dfs(node.left)
            # Append current node.val
            ans.append(node.val)
            # If node.right exists dfs on right child
            if node.right:
                dfs(node.right)
        # If root is not None run dfs else return None
        if root:
            dfs(root)
        else:
            return None
        # Return kth smallest val from sorted list
        return ans[k - 1]
