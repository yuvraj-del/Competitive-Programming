"""
Problem: 48. Rotate Image
Date Completed: 5/30/2025
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        # Flip the matrix horizontally
        for i in range(len(matrix)):
            for j in range(len(matrix[0])//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix[0]) - 1 - j]
                matrix[i][len(matrix[0]) - 1 - j] = temp
