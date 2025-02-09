"""
Level: Medium
Link: https://leetcode.com/problems/count-number-of-bad-pairs/
Tags: array, hash-table, math, counting
Description:
You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad
pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.
"""
class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        vals = {}
        for i, j in enumerate(nums):
            if i-j in vals:
                vals[i-j] += 1
            else:
                vals[i-j] = 0
        return int((len(nums)*(len(nums)-1))/2 - sum((((val+1)*val)/2) for val in vals.values() if val ))