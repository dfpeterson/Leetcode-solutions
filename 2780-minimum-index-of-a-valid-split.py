"""
Level: Medium
Link: https://leetcode.com/problems/minimum-index-of-a-valid-split/
Tags: array, hash-table, sorting
Description:
An element x of an integer array arr of length m is dominant if more than half
the elements of arr have a value of x.

You are given a 0-indexed integer array nums of length n with one dominant
element.

You can split nums at an index i into two arrays nums[0, ..., i] and
nums[i + 1, ..., n - 1], but the split is only valid if:
 * 0 <= i < n - 1
 * nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.

Here, nums[i, ..., j] denotes the subarray of nums starting at index i and
ending at index j, both ends being inclusive. Particularly, if j < i then
nums[i, ..., j] denotes an empty subarray.

Return the minimum index of a valid split. If no valid split exists, return -1.
"""
from statistics import mode
class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        modenum = mode(nums)
        l, r = 0, nums.count(modenum)
        rc = len(nums)
        for a in range(rc):
            if nums[a] == modenum:
                l += 1
                r -= 1
            if l > ((a + 1) // 2) and r > ((rc - a - 1) // 2):
                return a
        return -1