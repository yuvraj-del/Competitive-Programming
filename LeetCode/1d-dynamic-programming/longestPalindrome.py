"""
Problem: 5. Longest Palindromic Substring
Date Completed: 7/24/2025
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Helper function, if offset = 0 check for even length palindromes, elif offset = 1 check for odd length 
        def helper(offset: int) -> str:
            ans = ""
            # Loops over all possible 2 or 3 length substrings
            for i in range(len(s) - 1 - offset):
                temp = s[i:i+2 + offset]
                j = 0
                # If the ends match its a palindrome and we can expand and check again
                while temp[0] == temp[-1]:
                    if len(temp) > len(ans):
                        ans = temp
                    j += 1
                    # Checking for a valid substring
                    if i - j < 0 or i + 2 + offset + j > len(s):
                        break
                    temp = s[i - j : i + 2 + offset + j]
            return ans
        # Even length Longest Palindromic Substring
        even = helper(0)
        # Odd length Longest Palindromic Substring
        odd = helper(1)

        # Return correct answer
        if 0 == len(even) == len(odd):
            return s[0]
        elif len(even) > len(odd):
            return even
        else:
            return odd
