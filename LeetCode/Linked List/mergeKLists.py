"""
Problem: 23. Merge k Sorted Lists
Date Completed: 6/17/2025
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Merging Two Lists (Code from mergeTwoLists.py in my repo)
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            ans = ListNode()
            node = ans
            while list1 != None and list2 != None:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next
            node.next = list1 if list1 != None else list2
            return ans.next

        # If the lists doesn't exist return None
        if len(lists) == 0:
            return None
        # Else res will be the result of k sorted lists
        res = lists[0]
        # Merge every list with res
        for i in range(1, len(lists)):
            res = mergeTwoLists(res, lists[i])
        
        return res
