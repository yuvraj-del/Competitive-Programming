"""
Problem: 206. Reverse Linked List
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Set the current and previous pointers
        curr = head
        prev = None
        # Iterate over the linked list
        while curr != None:
            # Store the next pointer
            x = curr.next
            # Set the next pointer to the previous one, essentially reversing that link
            curr.next = prev
            # Move forward in the list
            prev = curr
            # Move to the next node, the link we broke
            curr = x
        return prev
