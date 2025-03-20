"""
Level: Medium
Link: https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
Tags: array, bit-manipulation, queue, sliding-window, prefix-sum
Description:
You are given a binary array nums.

You can do the following operation on the array any number of times (possibly
zero):
 * Choose any 3 consecutive elements from the array and flip all of them.

Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums
equal to 1. If it is impossible, return -1.
"""
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        change_count = 0
        for n in range(len(nums)-2):
            if not nums[n]:
                change_count += 1
                nums[n] = not nums[n]
                nums[n + 1] = not nums[n + 1]
                nums[n + 2] = not nums[n + 2]
        if not nums[-1] or not nums[-2]:
            return -1
        return change_count