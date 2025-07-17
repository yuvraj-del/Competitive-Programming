"""
Problem: 215. Kth Largest Element in an Array
Date Completed: 7/17/2025
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Turn nums into min-Heap
        heapq.heapify(nums)
        # While nums is bigger than k remove elements
        while len(nums) > k:
            heapq.heappop(nums)
        # Return first element, which will be the k-th largest
        return nums[0]
