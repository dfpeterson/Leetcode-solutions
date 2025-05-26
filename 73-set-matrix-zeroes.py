"""
Level: Medium
Link: https://leetcode.com/problems/set-matrix-zeroes/
Tags: array, hash-table, matrix
Description:
Given an m x n integer matrix matrix, if an element is 0, set its entire row
and column to 0's.

You must do it in place.
"""
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 0:
                    zero_rows.add(x)
                    zero_cols.add(y)
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if x in zero_rows or y in zero_cols:
                    matrix[x][y] = 0