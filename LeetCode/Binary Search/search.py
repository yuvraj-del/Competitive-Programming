"""
Problem: 33. Search in Rotated Sorted Array
Date Completed: 6/12/2025
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        # Binary Search algorithm
        def bsearch(l: int, r: int) -> int:
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        #Find the index of pivot in the rotated array
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
        
        # Perform binary search on the half with target 
        if nums[-1] >= target >= nums[l]:
            return bsearch(l, len(nums) - 1)
        else:
            return bsearch(0, l - 1)
