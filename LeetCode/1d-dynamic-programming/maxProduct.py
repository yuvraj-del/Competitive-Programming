"""
Problem: 152. Maximum Product Subarray
Date Completed: 7/25/2025
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Set ans to the min possible value
        ans = float("-inf")
        # Our products going forward or backwards in nums
        forward = 1
        backward = 1
        # Loop over every value in nums
        for i in range(len(nums)):
            # Multiply forward by current value, if forward is 0 make it current value
            forward = forward * nums[i] if forward else nums[i]
            # Multiply backward by current value, if backward is 0, make it current value
            backward = backward * nums[len(nums) - 1 - i] if backward else nums[len(nums) - 1 - i]
            # The max found so far
            ans = max(ans, forward, backward)
        return ans
