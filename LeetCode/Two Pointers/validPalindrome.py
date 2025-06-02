"""
Problem: 125. Valid Palindrome
Date Completed: 6/2/2025
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Creates new string, ans, which only contains alphanumeric characters
        ans = "".join(i.lower() for i in s if i.isalnum())
        # Check for a valid palindrome
        for i in range(len(ans) // 2):
            if ans[i] != ans[len(ans) - 1 - i]:
                return False
        return True
