"""
Level: Medium
Link: https://leetcode.com/problems/count-complete-subarrays-in-an-array/
Tags: array, hash-table, sliding-window
Description:
You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is
satisfied:
 * The number of distinct elements in the subarray is equal to the number of
   distinct elements in the whole array.

Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.
"""
from collections import defaultdict
class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        K = len(nums)
        allnums = set(nums)
        num_count = defaultdict(int)
        p1, p2 = 0, 0
        ans = 0
        while p2 < K:
            num_count[nums[p2]] += 1
            while len(num_count) == len(allnums):
                ans += K - p2
                num_count[nums[p1]] -= 1
                if num_count[nums[p1]] == 0:
                    del num_count[nums[p1]]
                p1 += 1
            p2 += 1
        return ans
