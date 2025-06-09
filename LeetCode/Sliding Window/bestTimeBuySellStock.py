"""
Problem: 121. Best Time to Buy and Sell Stock
Date Completed: 6/9/2025
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = prices[0]
        ans = 0
        for i in range(len(prices)):
            # Update the min price seen so far
            cost = min(cost, prices[i])
            # If the current price is higher than the min price
            if prices[i] > cost:
                # Then calculate max profit
                ans = max(ans, prices[i] - cost)
        return ans
