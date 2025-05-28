"""
Problem: 49. Group Anagrams
Date Completed: 5/28/2025
"""

# Import defaultdict from collections, my main tool to solve this problem
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict
        ans = defaultdict(list)
        
        # Iterate through each string in strs list
        for i in strs:
            # Use a sorted version of the word as a key
            ans[tuple(sorted(i))].append(i)
        
        # Return the group anagrams
        return list(ans.values())
