"""
Problem: 268. Missing Number
Date Completed: 7/28/2025
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # If we find the sum of all numbers 0-n and then subtract the sum of nums then we will find the missing num
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)
