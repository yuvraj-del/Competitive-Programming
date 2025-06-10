"""
Problem: 424. Longest Repeating Character Replacement
Date Completed: 6/10/2025
"""

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # The frequency of each char in window
        mostPop = defaultdict(int)
        # The frequency of the most popular char in the window
        currPop = 0
        l = 0
        ans = 0
        for i in range(len(s)):
            # Add the current char to mostPop
            mostPop[s[i]] += 1
            # Update if new most popular is found
            currPop = max(currPop, mostPop[s[i]])
            # If replacements is bigger than k, shrink left pointer
            while i + 1 - l - currPop > k:
                # Decrease the count of the char at the left pointer
                mostPop[s[l]] -= 1
                l += 1
            # Update the answer with max length
            ans = max(ans, i + 1 - l)
        return ans
