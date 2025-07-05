"""
Level: Easy
Link: https://leetcode.com/problems/longest-harmonious-subsequence/
Tags: array, hash-table, sliding-window, sorting, counting
Description:
We define a harmonious array as an array where the difference between its
maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious
subsequence among all its possible subsequences.
"""
from collections import Counter
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        num_count = Counter(nums)
        ans = 0
        for num in num_count:
            if num + 1 in num_count:
                ans = max(ans, num_count[num] + num_count[num + 1])
        return ans