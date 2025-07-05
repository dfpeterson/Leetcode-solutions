"""
Level: Easy
Link: https://leetcode.com/problems/find-the-lucky-integer-in-the-array/
Tags: array, hash-table, counting
Description:
Given an array of integers arr, a lucky integer is an integer that has a
frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer
return -1.
"""
from collections import Counter
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        lucky = [num1 for num1, num2 in Counter(arr).items() if num1 == num2]
        return max(lucky) if lucky else -1