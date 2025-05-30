"""
Problem: 54. Spiral Matrix
Date Completed: 5/30/2025
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # Define boundaries
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        ans = []
        for _ in range(len(matrix) * len(matrix[0])):
            
            # Iterate over all 4 moves
            for i in range(4):

                # If at any point we have all values stop
                if len(ans) == len(matrix) * len(matrix[0]):
                    return ans

                # Collect values left to right
                if i == 0:
                    for j in range(left, right + 1):
                        ans.append(matrix[top][j])
                    top += 1

                # Collect values top to bottom
                if i == 1:
                    for j in range(top, bottom + 1):
                        ans.append(matrix[j][right])
                    right -= 1

                # Collect values right to left
                if i == 2:
                    for j in range(right, left - 1, -1):
                        ans.append(matrix[bottom][j])
                    bottom -= 1

                # Collect values bottom to top
                if i == 3:
                    for j in range(bottom, top - 1, -1):
                        ans.append(matrix[j][left])
                    left += 1

        return ans
