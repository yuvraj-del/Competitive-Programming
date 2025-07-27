"""
Problem: 190. Reverse Bits
Date Completed: 7/27/2025
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        # Make n into a str of its bin version with leading 0s such that its length is 32
        n = str(bin(n)[2:]).zfill(32)
        ans = [0] * 32
        # For the first half of n
        for i in range(len(n) // 2):
            # Swap bits to reverse the string and store it in ans
            ans[i], ans[32 - 1 - i] = n[32 - 1 - i], n[i]
        # Turn the ans arr into a base-10 and return it
        return int("".join(ans), 2)
