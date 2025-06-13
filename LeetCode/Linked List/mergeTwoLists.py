"""
Problem: 21. Merge Two Sorted Lists
Date Completed: 6/13/2025

Notes:
- Solution inspired by NeetCode
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create ans linked list
        ans = ListNode()
        node = ans

        # Keep adding nodes until no more nodes are left in either list
        while list1 != None and list2 != None:
            # The next val in ans list is list1 if list1 is smaller than list2
            if list1.val < list2.val:
                node.next = list1
                # Move forward in list1
                list1 = list1.next
            # The next val in ans list is list2 if list2 is less than or equal to list1
            else:
                node.next = list2
                # Move forward in list2
                list2 = list2.next
            # Move forward in ans list
            node = node.next

        # If we have added the entirety of one list, then we add the remaining part of the other
        node.next = list1 if list1 != None else list2

        return ans.next
