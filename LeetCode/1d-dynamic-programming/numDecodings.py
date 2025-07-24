"""
Problem: 91. Decode Ways
Date Completed: 7/24/2025

Notes:
- Code based on NeetCode's solution
"""

class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {len(s) : 1}

        def ways(i: int) -> int:
            # If we already calculated ways at that index return it so as to not calculate it again
            if i in dp:
                return dp[i]
            # If at current index the num is 0 return 0 because there are 0 ways to decode it
            if s[i] == "0":
                return 0
            # Dont combined the next digit and keep finding ways
            temp = ways(i + 1)
            # And we can also combine if a value exists and is between 10 and 26
            if i + 1 < len(s) and 10 <= int(s[i: i + 2]) <= 26:
                temp += ways(i + 2)
            # Change dp to be equal to the number of values calculated at that index
            dp[i] = temp
            return temp
            
        return ways(0)
