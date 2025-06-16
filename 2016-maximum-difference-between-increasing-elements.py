"""
Level: Easy
Link: https://leetcode.com/problems/maximum-difference-between-increasing-elements/
Tags: array
Description:
Given a 0-indexed integer array nums of size n, find the maximum difference
between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n
and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
"""
class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        l = 0
        ans = -1
        for r in range(len(nums)):
            if nums[l] > nums[r]:
                l = r
            if nums[l] < nums[r]:
                ans = max(ans, nums[r] - nums[l])
        return ans
