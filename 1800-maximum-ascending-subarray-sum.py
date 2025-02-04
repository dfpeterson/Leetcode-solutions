"""
Level: Easy
Link: https://leetcode.com/problems/maximum-ascending-subarray-sum/
Tags: array, greedy
Description:
Given an array of positive integers nums, return the maximum possible sum of an
ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i
where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is
ascending.
"""
class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        current, maxsum, last, = 0, 0, 0
        for num in nums:
            if num <= last:
                current = num
            else:
                current += num
            maxsum = max(maxsum, current)
            last = num
        return maxsum