"""
Problem: 139. Word Break
Date Completed: 7/26/2025
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def helper(i: int) -> int:
            # If we already calculated if it is possible then return it so as to not calculate it again
            if i in dp:
                return dp[i]
            # If we reached the end of the string return True
            if i == len(s):
                dp[i] = True
                return True
            # For every word in wordDict 
            for word in wordDict:
                # Check if it is the next word in s after index i
                if s[i:i+len(word)] == word:
                    # If i + len(word) is True then i also has to be True
                    if helper(i + len(word)):
                        dp[i] = True
                        return True
            # If no words work then return False for this index
            dp[i] = False
            return False
        # Run helper(0) so we can start checking the string at index 0
        return helper(0)
