"""
Level: Easy
Link: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
Tags: array
Description:
Given a 0-indexed integer array nums of length n and an integer k, return the
number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and
(i * j) is divisible by k. 
"""
from collections import defaultdict
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pair_locs = defaultdict(list)
        pairs = 0
        for m in range(len(nums)):
            if m % k == 0:
                pairs += len(pair_locs[nums[m]])
            else:
                pairs += sum([(m * n) % k == 0 for n in pair_locs[nums[m]]])
            pair_locs[nums[m]].append(m)
        return pairs