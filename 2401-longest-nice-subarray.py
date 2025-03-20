"""
Level: Medium
Link: https://leetcode.com/problems/longest-nice-subarray/
Tags: array, bit-manipulation, sliding-window
Description:
You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements
that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.
"""
class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        nice = nums[0]
        p1 = 0
        nicest = 1
        for p2 in range(1,len(nums)):
            if nice & nums[p2]:
                while p1 < p2 and nice & nums[p2]:
                    nice -= nums[p1]
                    p1 += 1
            nice += nums[p2]
            nicest = max(nicest, p2 - p1 + 1) 
        return nicest