"""
Problem: 66. Plus One
Date Completed: 7/29/2025
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Helper function
        def helper(add: int, i: int) -> None:
            # Add to digits[i], +1 is carry or 0 is no carry
            digits[i] += add
            # If digits[i] is 10 we need to carry
            if digits[i] == 10:
                # Make it 0
                digits[i] = 0
                # If there is a valid index to carry to, run helper again with add: 1
                if i > 0:
                    helper(1, i - 1)
                else:
                    # If there is no valid index to carry to, insert a 1 at index 0
                    digits.insert(0, 1)
        # Run helper at the end of the list
        helper(1, len(digits) - 1)
        # Return list + 1
        return digits
