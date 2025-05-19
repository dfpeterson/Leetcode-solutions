"""
Level: Easy
Link: https://leetcode.com/problems/type-of-triangle/
Tags: array, math, sorting
Description:
You are given a 0-indexed integer array nums of size 3 which can form the sides
of a triangle.
 * A triangle is called equilateral if it has all sides of equal length.
 * A triangle is called isosceles if it has exactly two sides of equal length.
 * A triangle is called scalene if all its sides are of different lengths.

Return a string representing the type of triangle that can be formed or "none"
if it cannot form a triangle.
"""
class Solution:
    def triangleType(self, nums: list[int]) -> str:
        a, b, c = nums
        if all([c < a + b, b < a + c, a < b + c]):
            return {0: 'scalene', 1: 'isosceles', 3: 'equilateral'}[sum([a == b, b == c, a == c])]
        return 'none'