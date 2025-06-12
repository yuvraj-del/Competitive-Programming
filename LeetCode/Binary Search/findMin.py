"""
Problem: 153. Find Minimum in Rotated Sorted Array
Date Completed: 6/12/2025
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Left and Right pointers for the binary search
        l = 0
        r = len(nums) - 1
        while l < r:
            # Calculate mid value
            mid = (l + r) // 2
            # If the mid value is less than right value than mim must be in left half of array
            if nums[mid] < nums[r]:
                r = mid
            # If the mid value if greater than right value than mim must be in right half of array
            elif nums[mid] > nums[r]:
                l = mid + 1
        return nums[l]
