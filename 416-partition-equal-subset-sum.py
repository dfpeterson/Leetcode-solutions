"""
Level: Medium
Link: https://leetcode.com/problems/partition-equal-subset-sum/
Tags: array, dynamic-programming
Description:
Given an integer array nums, return true if you can partition the array into
two subsets such that the sum of the elements in both subsets is equal or
false otherwise.
"""
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        max_val = sum(nums)
        goal = max_val // 2

        if max_val % 2 or goal < max(nums):
            return False
        if goal == max(nums):
            return True

        combo_set = set([0])
        for k in range(len(nums) - 1, -1, -1):
            hold_set = set()
            for val in combo_set:
                hold_set |= set([val + nums[k], val])
            if goal in hold_set:
                return True
            combo_set = hold_set
        return goal in combo_set