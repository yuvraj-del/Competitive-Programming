"""
Problem: 271. Encode and Decode Strings
Date Completed: 5/29/2025
"""

class Solution:

    
    def encode(self, strs: List[str]) -> str:
        ans = []
        for s in strs:
            # Append length of string, delimiter, and string
            ans.append(str(len(s)) + "#" + s)
        # Returns in one string
        return "".join(ans)

    
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            # Find the position of the delimiter
            while s[j] != "#":
                j += 1
            # The length of the next string
            size = int(s[i:j])
            j += 1  # Skip past the delimiter
            # Append the string
            ans.append(s[j: j + size])
            # Set i to end of string
            i = j + size
        return ans
