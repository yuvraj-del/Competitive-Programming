"""
Problem: 76. Minimum Window Substring
Date Completed: 6/11/2025
"""

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initializes ans, the left and right pointers of ans string
        ans = [-1, -1]
        # Initializes done, count of how many chars are fully collected
        done = 0
        # Initializes lenT, number of unique chars needed from t
        lenT = len(set(t))
        # Frequency of each char in t
        tMap = defaultdict(int)
        for i in t:
            tMap[i] += 1
            
        l = 0
        # Frequency of each char in window
        windowMap = defaultdict(int)
        for i in range(len(s)):
            # Add current char to window
            windowMap[s[i]] += 1
            # If char in t and we have collected enough then add to done
            if s[i] in tMap and windowMap[s[i]] == tMap[s[i]]:
                done += 1
            # If all chars are collected
            if done == lenT:
                # Try to shrink the window
                while done == lenT:
                    # Update ans if window is smaller
                    if ans == [-1, -1] or i + 1 - l < ans[1] - ans[0]:
                        ans = [l, i + 1]
                    # Remove char
                    windowMap[s[l]] -= 1
                    # If window not valid, done -= 1
                    if s[l] in tMap and windowMap[s[l]] < tMap[s[l]]:
                        done -= 1
                    # Shrink window
                    l += 1

        if ans == [-1, -1]:
            return ""
        return s[ans[0]:ans[1]]
