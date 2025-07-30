"""
Problem: 50. Pow(x, n)
Date Completed: 7/29/2025
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base cases
        # 0 to any power is 0
        if x == 0:
            return 0
        # Any number to the power of 0 is 1
        if n == 0:
            return 1
        # Helper function
        def helper(x: float, n: int) -> float:
            # Any number to the power of 1 is itself
            if n == 1:
                return x
            # Any number to the power of 2 is number * number
            if n == 2:
                return x * x
            # Store temp which is x ^ n // 2
            temp = helper(x, n // 2)
            # If n is ever just return temp squared
            if n % 2 == 0:
                return temp * temp
            # Else multiply by x once more because of floor division
            else:
                return temp * temp * x
        # If the power is positive return normally
        if n > 0:
            return helper(x, n)
        # Else return 1 over the output from helper
        else:
            return 1 / helper(x, -n)
