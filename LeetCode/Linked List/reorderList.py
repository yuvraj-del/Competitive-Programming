"""
Problem: 143. Reorder List
Date Completed: 6/15/2025
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Finds the middle of the linked list
        single = head
        double = head
        prevMid = None

        while double != None and double.next != None:
            prevMid = single
            single = single.next
            double = double.next.next
        
        # Cuts off the first half from the second half
        if prevMid:
            prevMid.next = None
        else:
            return None
        
        # Reverses the second half of list
        curr = single
        prev = None
        while curr != None:
            x = curr.next
            curr.next = prev
            prev = curr
            curr = x
        
        # Merges two lists together
        l = head
        r = prev

        while l != None and r != None:
            l_next = l.next
            r_next = r.next

            l.next = r
            if not l_next:
                break
            r.next = l_next

            l = l_next
            r = r_next

        return None
