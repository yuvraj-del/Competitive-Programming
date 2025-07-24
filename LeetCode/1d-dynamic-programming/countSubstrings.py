"""
Problem: 647. Palindromic Substrings
Date Completed: 7/24/2025
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        # See file longestPalindrome.py for the explanation for this function
        def helper(offset: int) -> int:
            ans = 0
            for i in range(len(s) - 1 - offset):
                temp = s[i:i+2 + offset]
                j = 0
                while temp[0] == temp[-1]:
                    # Only change from previous file:
                    # Now increment for every valid palindrome found
                    ans += 1
                    j += 1
                    if i - j < 0 or i + 2 + offset + j > len(s):
                        break
                    temp = s[i - j : i + 2 + offset + j]
            return ans
        # Return all even + all odd palindromes + len(s), because every char is also a palindrome
        return helper(0) + helper(1) + len(s)
