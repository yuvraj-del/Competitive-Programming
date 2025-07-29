"""
Problem: 202. Happy Number
Date Completed: 7/29/2025
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        # Create a dict with all the values we have seen so far
        seen = {}
        # If we havent seen the current value calculate the sum of the squares of its digits
        while n not in seen:
            # Add n to seen
            seen[n] = True
            # Calculate the sum of the squares of its digits
            n = sum(int(i) ** 2 for i in str(n))
            # If n is 1 its a happy number
            if n == 1:
                return True
        # If we have already seen the value its an inf loop and it will never be happy
        return False
