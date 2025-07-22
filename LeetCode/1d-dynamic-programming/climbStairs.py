"""
Problem: 70. Climbing Stairs
Date Completed: 7/22/2025
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Create a list with max(n+1, 3) so we can always assign index 1 and 2
        fib = [0] * max(n+1, 3)
        # Set base cases
        fib[1], fib[2] = 1, 2
        # Until we reach index n keep filling in fib with the sum of previous 2 indices
        for i in range(3, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        # Return index n in fib
        return fib[n]
