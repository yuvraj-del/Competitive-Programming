"""
Problem: 703. Kth Largest Element in a Stream
Date Completed: 7/16/2025

Notes:
- Code based on NeetCode's solution
"""

class KthLargest:
    # Constructor
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        # Turn nums into a min-heap
        heapq.heapify(self.nums)
        # If len of heap is greater than k keep removing the smallest value
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
    # Add function
    def add(self, val: int) -> int:
        # Add current value
        heapq.heappush(self.nums, val)
        # If we have more than k elements in heap remove the smallest
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # Return the k-th largest value
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
