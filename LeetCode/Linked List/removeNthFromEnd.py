"""
Problem: 19. Remove Nth Node From End of List
Date Completed: 6/17/2025
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize fast and slow pointers and a size counter
        fast = head
        slow = head
        size = 1
        # Move fast pointer n-1 nodes ahead of slow
        for _ in range(n-1):
            size += 1
            fast = fast.next
        # Initialize a prev pointer
        prev = head
        # Go through the list until fast reaches the last node
        while fast.next != None:
            # Update prev and move slow and fast forward one node
            prev = slow
            slow = slow.next
            fast = fast.next
            # Update size
            size += 1
        # If n is equal to the size of the list
        if size == n:
            # Return the list starting from the second node
            if head.next:
                return head.next
            # Else return None
            else:
                return None
        else:
            # Remove the nth node from the end by updating links
            prev.next = slow.next
            return head
