"""
Problem: 128. Longest Consecutive Sequence
Date Completed: 5/29/2025
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = set(nums)
        ans = 0
        for i in x:
            # If i - 1 is not in the set, i is the start of a new consecutive chain
            if i - 1 not in x:
                j = 0
                # Count how many consecutive numbers after i
                while i + j in x:
                    j += 1
                ans = max(ans, j)
        return ans
