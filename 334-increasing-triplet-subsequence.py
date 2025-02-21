"""
Level: Medium
Link: https://leetcode.com/problems/increasing-triplet-subsequence/
Tags: array, greedy
Description: 
Given an integer array nums, return true if there exists a triple of indices
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
indices exists, return false.
"""
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        last_set = [float('inf'), float('inf')]
        trigger = float('inf')
        for z in nums:
            if last_set[0] < last_set[1] < z:
                return True
            if z < trigger:
                trigger = z
            if trigger < last_set[0] and trigger < z:
                last_set = [trigger, z]
            if z > last_set[0] and z < last_set[1] and z != trigger:
                last_set[1] = z
        return False