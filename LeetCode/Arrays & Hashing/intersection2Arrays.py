"""
Problem: 349. Intersection of Two Arrays
Date Completed: 5/27/2025
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Uses "&" which gets intersection of 2 sets and then casts to list for the return type
        return list(set(nums1) & set(nums2))
