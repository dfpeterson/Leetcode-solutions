"""
Level: Medium
Link: https://leetcode.com/problems/count-the-number-of-good-subarrays/
Tags: array, hash-table, sliding-window
Description:
Given an integer array nums and an integer k, return the number of good
subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such
that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.
"""
from collections import defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)
        num_counts = defaultdict(int)
        found_pairs = 0
        good_pairs = 0
        l = 0
        for r in range(N):
            found_pairs += num_counts[nums[r]]
            num_counts[nums[r]] += 1 
            while found_pairs >= k:
                good_pairs += N - r
                num_counts[nums[l]] -= 1
                found_pairs -= num_counts[nums[l]]
                l += 1
        return good_pairs
