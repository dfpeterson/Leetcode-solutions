"""
Level: Medium
Link: https://leetcode.com/problems/first-completely-painted-row-or-column/
Tags: array, hash-table, matrix
Description:
You are given a 0-indexed integer array arr, and an m x n integer matrix mat.
arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat
containing the integer arr[i].

Return the smallest index i at which either a row or a column will be
completely painted in mat.
"""
class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        mat2 = {num: (x, y) for y, row in enumerate(mat) for x, num in enumerate(row)}
        row_count = len(mat)
        col_count = len(mat[0])
        row_check = {}
        col_check = {}
        for j, k in enumerate(arr):
            x, y = mat2[k]
            row_check[x] = row_check.get(x, 0) + 1
            col_check[y] = col_check.get(y, 0) + 1
            if row_check[x] == row_count or col_check[y] == col_count:
                return j