"""
Problem: 1. Two Sum
Date Completed: 5/27/2025
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate through each element
        for i in range(len(nums)):
            # Iterate through the elements after the current element
            for j in range(i + 1, len(nums)):
                # Check if sum equals target, then return indices
                if nums[i] + nums[j] == target:
                    return [i, j]
