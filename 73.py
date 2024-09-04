"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_col, zero_row = [], []
        col, row = len(matrix), len(matrix[0])

        for c in range(col):
            for r in range(row):
                if matrix[c][r] == 0:
                    zero_row.append(r)
                    zero_col.append(c)

        for c in range(col):
            for r in range(row):
                if r in zero_row or c in zero_col:
                    matrix[c][r] = 0


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
Solution().setZeroes(matrix)
print(matrix)
