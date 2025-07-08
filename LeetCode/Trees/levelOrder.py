"""
Problem: 102. Binary Tree Level Order Traversal
Date Completed: 7/8/2025
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: if empty tree return []
        if not root:
            return []

        # Initialize queue and ans lists    
        queue = []
        ans = []

        # Add root to queue
        queue.append(root)

        # Breadth First Search
        while queue:
            # All vals in current row
            curr = []
            # Add all vals in row to curr list and add all children to queue list
            for i in range(len(queue)):
                node = queue.pop(0)
                curr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Append curr to ans 
            ans.append(curr)
        
        return ans
