"""
Level: Easy
Link: https://leetcode.com/problems/special-array-with-sum-equals-target/
Tags: array
Description:
An array is considered special if every pair of its adjacent elements contains
two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special
array, otherwise, return false.  
"""
class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        for a, b in zip(nums, nums[1:]):
            if a % 2 == b % 2:
                return False
        return True