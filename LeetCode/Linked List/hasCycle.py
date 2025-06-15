"""
Problem: 141. Linked List Cycle
Date Completed: 6/15/2025
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers at the start of the list
        single = head
        double = head
        
        # While the pointer in the lead and the one step ahead of it aren't equal to None
        while double != None and double.next != None:
            # Move the single pointer one step
            single = single.next
            # Move the double pointer two steps
            double = double.next.next
            # If we ever get a match, the faster one has essentially lapped the slower one and we found a cycle
            if single == double:
                return True
        return False
