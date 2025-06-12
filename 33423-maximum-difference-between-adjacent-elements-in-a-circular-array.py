"""
Level: Easy
Link: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
Tags: array
Description:
Given a circular array nums, find the maximum absolute difference between
adjacent elements.

Note: In a circular array, the first and last elements are adjacent.
"""
class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        return max([abs(nums[i - 1] - nums[i]) for i in range(len(nums))])