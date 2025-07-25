"""
Level: Easy
Link: https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/
Tags: array, hash-table, greedy
Description:
You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it
empty. After performing the deletions, select a subarray of nums such that:
 * All elements in the subarray are unique.
 * The sum of the elements in the subarray is maximized.

Return the maximum sum of such a subarray.
"""
class Solution:
    def maxSum(self, nums: list[int]) -> int:
        checked = set(nums)
        if max(checked) < 0:
            return max(checked)
        return sum({k for k in checked if k >= 0})