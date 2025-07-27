"""
Problem: 213. House Robber II
Date Completed: 7/22/2025
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        # If there is only 1 house then rob that one
        if len(nums) == 1:
            return nums[0]
        # If there is only 2 houses then rob the one with more money
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        # Helper function, if offset = 0 then we skip the last house, elif offset = 1 then we skip the first house
        def robCheck(offset: int) -> int:
            # Create arr with length of nums - 1 because we either take out the first or last house
            arr = [0] * (len(nums) - 1)
            # Set base cases for arr
            arr[0], arr[1] = nums[0 + offset], max(nums[0 + offset], nums[1 + offset])
            # Loop over the remaining houses in arr
            for i in range(2 + offset, len(nums) - 1 + offset):
                # Either rob current house + max amount 2 indices before it
                # Or don't rob and keep the max amount 1 index before
                arr[i - offset] = max(nums[i] + arr[i-2 - offset], arr[i-1 - offset])
            # Return max amount
            return arr[-1]
        # Return max amount between the 2 scenarios
        return max(robCheck(0), robCheck(1))
