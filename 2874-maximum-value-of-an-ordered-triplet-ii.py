"""
Level: Medium
Link: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/
Tags: array
Description:
You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that
i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to
(nums[i] - nums[j]) * nums[k].
"""
class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        a = 0
        max_diff = 0
        max_abc = 0
        for p in nums:
            max_abc = max(max_abc, (max_diff) * p)
            a = max(a, p)
            max_diff = max(max_diff, a - p)
        return max_abc