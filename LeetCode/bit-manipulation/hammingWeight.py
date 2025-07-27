"""
Problem: 191. Number of 1 Bits
Date Completed: 7/27/2025
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        # Bin turns our int n into a binary number
        for i in bin(n)[2:]:
            # Count number of 1's in the binary version of n
            if i == "1":
                ans += 1
        # Return the count
        return ans
