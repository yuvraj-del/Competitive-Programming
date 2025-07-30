"""
Problem: 43. Multiply Strings
Date Completed: 7/30/2025
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Base case, if either is 0 return 0
        if num1 == "0" or num2 == "0":
            return "0"
        # Make sure len(num1) is bigger than len(num2) else swap them
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        # Multiply num1 with a single digit of num2
        def mul(num1: str, num2: int) -> str:
            digits = [i for i in num1]
            temp = []
            carry = 0
            # For every digit in num1
            for i in reversed(digits):
                # Multiply and add carry
                product = int(i) * num2 + carry
                # Insert only the ones place of product
                temp.insert(0, str(product % 10))
                # Make carry equal to the tens place
                carry = product // 10
            # If we still have a carry after all digits then add it to the start
            if carry > 0:
                temp.insert(0, str(carry))
            # Return the str of num1 * a digit of num2
            return "".join(temp)
        # Make a res array
        res = []
        tens = 0
        # Build res array with all the products of num1 and digits of num2 with sufficient zeros at the end
        for i in reversed(num2):
            res.append(mul(num1, int(i)) + "0" * tens)
            tens += 1
        # Add all the strings in res together
        def add(nums: List[str]) -> str:
            # Create ans array
            ans = [0] * (len(nums[-1]) + 1)
            carry = 0
            # For every digit in answer
            for i in range(len(ans) - 1, 0, -1):
                total = carry
                # Add to total for all nums that have the current digit
                for j in range(len(nums)):
                    idx = len(nums[j]) - 1 - (len(ans) - 1 - i)
                    # If the current num has the digit add it
                    if idx >= 0:
                        total += int(nums[j][idx])
                # Keep only the ones place and store the carry
                ans[i] = total % 10
                carry = total // 10
            # Add any remaining carry
            ans[0] = carry
            # Strip any zeros
            result = "".join(map(str, ans)).lstrip("0")
            # Return if we have a valid result
            return result if result else "0"
        # Return answer
        return add(res)
