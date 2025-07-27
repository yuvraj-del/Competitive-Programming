"""
Problem: 322. Coin Change
Date Completed: 7/25/2025

Notes:
- Solution inspired by NeetCode
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Set base case: 0 coins needed to make 0 amount
        dp = {0: 0}
        # Helper function to calculate the min amount of coins need to make i amount
        def helper(i: int) -> int:
            # If we already calculated coins at that index return it so as to not calculate it again
            if i in dp:
                return dp[i]
            # Set the fewest coin to max int
            few = float("inf")
            # Go through every coin we have
            for c in coins:
                # If the coin is a valid
                if i - c >= 0:
                    # Then test to see if its less then any other path
                    # And keep continuing on other paths
                    few = min(few, helper(i - c) + 1)
            # Store and return fewest coins for this amount
            dp[i] = few        
            return dp[i]
        # Calculate fewest coins for amount
        ans = helper(amount)
        # If there is a valid ans return it or else return -1
        if ans != float("inf"):
            return ans
        else:
            return -1
