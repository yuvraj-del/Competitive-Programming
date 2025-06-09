"""
Problem: 11. Container With Most Water
Date Completed: 6/9/2025
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize l and r pointers
        l = 0
        r = len(height) - 1
        # Set initial area
        ans = min(height[l], height[r]) * (r - l)
        while l < r:
            # Move the shorter pointer in hope to find a bigger area
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            # Set ans to max area found so far
            ans = max(ans, min(height[l], height[r]) * (r - l))
        return ans
