"""
Problem: 7. Reverse Integer
Date Completed: 7/29/2025
"""

class Solution:
    def reverse(self, x: int) -> int:
        # Declare ans and n which is the abs of x
        ans = 0
        n = abs(x)
        # If n is 0 then reverse is also 0, so return 0
        if n == 0:
            return 0
        # Else we need to build ans
        else:
            while n > 0:
                # Multiply ans by 10 to shift digits left, then add last digit of n
                ans = ans * 10 + n % 10
                # Remove the last digit from n
                n //= 10
        
        # If x was negative make ans negative again
        ans = ans if x > 0 else -ans
        # Check if answer goes out of bounds
        if ans > 2 ** 31 - 1 or ans < (-2) ** 31:
            return 0
        else:
            # Else return ans
            return ans
