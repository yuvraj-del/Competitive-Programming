"""
Problem: 238. Product of Array Expect Self
Date Completed: 5/28/2025
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize right and left product prefix arrays
        right = [1]
        left = [1]
        # Build prefix products from the left and the right
        for i in range(len(nums)):
            right.append(nums[i] * right[i])
            left.append(nums[len(nums) - 1 - i] * left[i])
        # Multiply the corresponding left and right products to form the result
        ans = []
        for i in range(len(nums)):
            ans.append(right[i] * left[len(nums) - 1 - i])
        return ans
