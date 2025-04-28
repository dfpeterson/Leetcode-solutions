"""
Level: Easy
Link: https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/
Tags: array
Description:
Given an integer array nums, return the number of of length 3 such that the sum
of the first and third numbers equals exactly half of the second number.
"""
class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        k = 0
        ans = 0
        while k < len(nums) - 2:
            if 2 * (nums[k] + nums[k + 2]) == nums[k + 1]:
                ans += 1
            k += 1
        return ans