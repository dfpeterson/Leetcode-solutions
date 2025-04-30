"""
Level: Easy
Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
Tags: array, math
Description:
Given an array nums of integers, return how many of them contain an even number
of digits.
"""
from math import ceil, log
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return sum([ceil(log(k +  1, 10)) % 2 == 0 for k in nums])