"""
Level: Easy
Link: https://leetcode.com/problems/count-total-number-of-colored-cells/
Tags: array, hash-table, math, matrix
Description:
You are given a 0-indexed 2D integer matrix grid of size n * n with values in
the range [1, n2]. Each integer appears exactly once except a which appears
twice and b which is missing. The task is to find the repeating and missing
numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and
ans[1] equals to b.
"""
class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        checks = set()
        for more in grid:
            setmore = set(more)
            if checks & setmore:
                a = (checks & setmore).pop()
            if len(setmore) != len(more):
                checkset = set()
                for z in more:
                    if z in checkset:
                        a = z
                        break
                    checkset.add(z)
            checks |= setmore
        if len(checks) == max(checks):
            b = len(checks) + 1
        else:
            b = (set(range(1, max(checks)+1)) - checks).pop()
        return [a, b]