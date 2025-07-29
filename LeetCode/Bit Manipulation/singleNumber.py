"""
Problem: 136. Single Number
Date Completed: 7/29/2025
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Create ans to store our answer
        ans = 0
        # For every element in nums
        for i in nums:
            # Apply XOR on ans and i
            # XOR because if a number appears twice it will cancel out to 0
            # So all duplicates cancel out and the single one stays
                ans ^= i
        return ans
