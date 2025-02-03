"""
Level: Easy
Link: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
Tags: array
Description:
You are given an array of integers nums. Return the length of the longest
subarray of nums which is either strictly increasing or strictly decreasing.
"""
class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        streak = 1
        max_streak = 1
        if nums[0] == nums[1]:
            direction = 0
        else:
            direction = (nums[1] - nums[0])/abs(nums[1] - nums[0])
        last_num = None
        for a in nums:
            if last_num:
                if a == last_num:
                    direction = 0
                    streak = 1
                else:
                    if (a- last_num)/abs(a- last_num) != direction:
                        streak = 1
                        direction = (a - last_num)/abs(a - last_num)
                    streak += 1
                    max_streak = max(max_streak, streak)
            print(a, last_num, max_streak, streak, direction)
            last_num = a
        return max_streak