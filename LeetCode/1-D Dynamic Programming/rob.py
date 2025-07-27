"""
Problem: 198. House Robber
Date Completed: 7/22/2025
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        # If there is only 1 house then rob that one
        if len(nums) == 1:
            return nums[0]
        # If there is only 2 houses then rob the one with more money
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        # Else create arr with the length of house on street
        arr = [0] * len(nums)
        # Set base cases
        arr[0], arr[1] = nums[0], max(nums[0], nums[1])
        # Repeat until we check every house
        for i in range(2, len(arr)):
            # Either rob current house + max amount 2 indices before it
            # Or don't rob and keep the max amount 1 index before
            arr[i] = max(nums[i] + arr[i - 2], arr[i - 1])
        return arr[-1]
