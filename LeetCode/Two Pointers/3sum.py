"""
Problem: 15. 3Sum
Date Completed: 6/4/2025

Notes:
- Solution inspired by NeetCode
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        # Fix one value
        for i in range(len(nums)):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Set left and right pointers
            l = i + 1
            r = len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                # If sum is too big decrease the right pointer
                if current_sum > 0:
                    r -= 1
                # If sum is too small increase the left pointer
                elif current_sum < 0:
                    l += 1
                else:
                    # Add valid triple to ans
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # Skip duplicates for the second number
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return ans
