"""
Problem: 3. Longest Substring Without Repeating Characters
Date Completed: 6/10/2025

Notes:
- Solution inspired by NeetCode
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        # Holds all unique chars in sliding window
        seen = set()
        for i in range(len(s)):
            # If a duplicate char is found, shrink window from left
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            # Add right pointer char to window
            seen.add(s[i])
            # Update the max length found so far
            ans = max(ans, i + 1 - l)
        return ans
