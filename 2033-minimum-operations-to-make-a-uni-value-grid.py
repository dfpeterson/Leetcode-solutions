"""
Level: Medium
Link: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
Tags: array, math, sorting, matrix
Description:
You are given a 2D integer grid of size m x n and an integer x. In one
operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is
not possible, return -1.
"""
class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        flat = []
        for k in grid:
            flat.extend(k)
        #find median
        #check that difference between all elements and median are % k == 0
        ml, mh = median_low(flat), median_high(flat)
        cl, ch = 0, 0
        for n in flat:
            if abs(n - ml) % x != 0 or abs(n - mh) % x != 0:
                return -1
            cl += abs(n - ml) // x
            ch += abs(n - mh) // x
        return min(cl, ch)