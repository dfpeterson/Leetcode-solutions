"""
Level: Easy
Link: https://leetcode.com/problems/two-sum/
Tags: array, hash-table
Description:
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for a, b in enumerate(nums):
            if target-b in nums[a+1:]:
                return [a,nums.index(target-b,a+1)]