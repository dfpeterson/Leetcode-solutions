"""
Level: Easy
Link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
Tags: array, binary-search, counting
Description:
Given an array nums sorted in non-decreasing order, return the maximum between
the number of positive integers and the number of negative integers.
 * In other words, if the number of positive integers in nums is pos and the
   number of negative integers is neg, then return the maximum of pos and neg.

Note that 0 is neither positive nor negative.
"""
class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pos, neg = len(nums), -1
        max_pos, min_neg = float('inf'), float('-inf')
        c = len(nums) // 2
        move = max(c, 1)
        while move > 0:
            if nums[c] < 0 and nums[c] >= min_neg:
                min_neg = nums[c]
                neg = c
            if nums[c] > 0 and nums[c] <= max_pos:
                max_pos = nums[c]
                pos = c
            if pos == 0 or neg == len(nums) - 1 or (nums[pos - 1] <= 0 and nums[neg + 1] >= 0):
                move = 0
            else:
                move = max(move // 2, 1)
            if neg < len(nums)-1 and nums[neg + 1] < 0:
                c += -move if nums[c] >= 0 else move
            else:
                c += move if nums[c] <= 0 else -move
        return max(neg + 1, len(nums) - pos)