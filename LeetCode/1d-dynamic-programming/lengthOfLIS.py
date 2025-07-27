"""
Problem: 300. Longest Increasing Subsequence
Date Completed: 7/27/2025
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def helper(i: int) -> int:
            # If we already calculated LIS at that index return it so as to not calculate it again
            if i in dp:
                return dp[i]
            # temp will be the len(LIS) after index i
            temp = 0
            # Loop over every element in nums after index i
            for j in range(i + 1, len(nums)):
                # If that number is larger than the number at index i
                if nums[j] > nums[i]:
                    # Then run helper again on the smaller problem (index j onwards)
                    # Update temp if we found a larger LIS
                    temp = max(temp, helper(j))
            # Set and return dp[i]
            # 1 + temp, because we need to keep increasing our count of the len of the LIS
            dp[i] = 1 + temp
            return dp[i]
        # Calculate the LIS starting at any index and return it
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, helper(i))
        return ans
