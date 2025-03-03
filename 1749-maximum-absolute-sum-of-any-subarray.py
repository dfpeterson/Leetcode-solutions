"""
Level: Medium
Link: https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
Tags: array, dynamic-programming
Description:
You are given an integer array nums. The absolute sum of a subarray [numsl,
numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:
 * If x is a negative integer, then abs(x) = -x.
 * If x is a non-negative integer, then abs(x) = x.
"""
class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        negs = 0
        sumaccum = 0
        min_plus, max_plus, = float('inf'), float('-inf')
        max_diff = 0
        for k in nums:
            sumaccum += k
            print(sumaccum)
            negs += 1 if negs < 0 else 0
            max_plus = max(max_plus, sumaccum)
            min_plus = min(min_plus, sumaccum)
            max_diff = max(max_diff, abs(max_plus - min_plus), abs(sumaccum))
        return max_diff