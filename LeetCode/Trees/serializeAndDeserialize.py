"""
Problem: 297. Serialize and Deserialize Binary Tree
Date Completed: 7/14/2025

Notes:
- Solution inspired by NeetCode
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # The serialized string
        ss = ""
        # Goes through tree using dfs
        def dfs(node):
            # Makes sure to change the nonlocal ss variable
            nonlocal ss
            # If node is null then add N, our version of None
            if not node:
                ss += "N,"
                return
            # Add node val to string
            ss += str(node.val) + ","
            # Continue dfs
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ss
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Get the serialized string
        tree = data.split(",")[:-1]
        # Index where we are at in tree
        i = 0
        # Build tree
        def dfsbuild():
            # Makes sure to access the nonlocal i var
            nonlocal i
            # If null node then increment i and dont build tree
            if tree[i] == "N":
                i += 1
                return
            # Build a new node
            node = TreeNode(int(tree[i]))
            # Increment i
            i += 1
            # Build left and right subtrees with dfs
            node.left = dfsbuild()
            node.right = dfsbuild()
            # Return node so it can be added to tree
            return node
        return dfsbuild()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
