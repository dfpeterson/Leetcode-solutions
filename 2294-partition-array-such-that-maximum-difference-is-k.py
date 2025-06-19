"""
Level: Medium
Link: https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
Tags: array, greedy, sorting
Description:
You are given an integer array nums and an integer k. You may partition nums
into one or more subsequences such that each element in nums appears in exactly
one of the subsequences.

Return the minimum number of subsequences needed such that the difference
between the maximum and minimum values in each subsequence is at most k.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining
elements.
"""
class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        l = 0
        ans = 1
        for i in range(len(nums)):
            if nums[i] - nums[l] > k:
                ans += 1
                l = i
        return ans