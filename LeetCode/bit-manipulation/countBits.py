"""
Problem: 338. Counting Bits
Date Completed: 7/27/2025
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Create ans array
        ans = [0] * (n + 1)
        # For every number up to n
        for i in range(n + 1):
            # Count the numbers of 1s and add it to ans
            ans[i] = bin(i).count('1')
        # Return ans
        return ans
