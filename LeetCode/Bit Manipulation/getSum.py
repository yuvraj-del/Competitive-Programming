"""
Problem: 371. Sum of Two Integers
Date Completed: 7/28/2025

Notes:
- Code based on NeetCode's solution
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask so that we can treat every number as a 32-bit number
        mask = 0b11111111111111111111111111111111
        # max_int is the largest positive 32-bit integer (2^31 - 1)
        max_int = mask >> 1

        while b != 0:
            # If both a and b have 1 then carry by adding a 1 to the left
            carry = (a & b) << 1
            # This is the "addition" without carrying
            a = (a ^ b) & mask
            # Store carry in b
            b = carry & mask

        # If a is greater than max_int its negative
        if a > max_int:
            # Return the negative version of a
            return ~(a ^ mask)
        else:
            # Else return plain a
            return a
