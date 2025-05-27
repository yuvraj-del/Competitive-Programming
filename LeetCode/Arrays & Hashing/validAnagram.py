"""
Problem: 242. Valid Anagram
Date Completed: 5/27/2025
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If both the sorted strings are the same then they must be anagrams
        return sorted(s) == sorted(t)
