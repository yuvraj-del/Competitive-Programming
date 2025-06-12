"""
Problem: 20. Valid Parentheses
Date Completed: 6/12/2025
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            # If the current char is an opening char add to stack
            if i in "({[":
                stack.append(i)
            # If the current char is a closing char and matches with the top of stack, pop the stack
            elif stack and (
                (i == ")" and stack[-1] == "(") or
                (i == "}" and stack[-1] == "{") or
                (i == "]" and stack[-1] == "[")
            ):
                stack.pop()
            # If we found a closing char without an opening char then string is not valid
            else:
                return False
        # Returns True if stack is empty else False
        return not stack
