"""
Problem: 347. Top K Frequent Elements
Date Completed: 5/28/2025
"""

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(list)
        # Iterate through each int in nums list
        for i in nums:
            # Fill in ans with frequency of each number
            ans[i].append(i)
        # Sort by length of values, take first k elements, and return only the keys
        return [key for key,_ in sorted(ans.items(), key=lambda x: len(x[1]), reverse=True)[:k]]
