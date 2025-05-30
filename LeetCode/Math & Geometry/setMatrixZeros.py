"""
Problem: 73. Set Matrix Zeroes
Date Completed: 5/30/2025
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Array r and c holds 0 if that row/col has 0, or 1 if it doesn't
        r = [1] * len(matrix)
        c = [1] * len(matrix[0])

        # Marks rows and cols that have 0
        for i in range(len(r)):
            for j in range(len(c)):
                if matrix[i][j] == 0:
                    r[i] = 0
                    c[j] = 0
        
        # Changes matrix based on marked rows and cols
        for i in range(len(r)):
            for j in range(len(c)):
                if r[i] == 0 or c[j] == 0:
                    matrix[i][j] = 0
