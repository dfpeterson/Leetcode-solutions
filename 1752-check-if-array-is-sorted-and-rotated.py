"""
Level: Easy
Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
Tags: array
Description:
Given an array nums, return true if the array was originally sorted in
non-decreasing order, then rotated some number of positions (including zero).
Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same
length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
"""
class Solution:
    def check(self, nums: list[int]) -> bool:
        rotates = 0
        start, end = nums[0], nums[-1]
        for a, b in zip(nums, nums[1:]):
            if a > b:
                rotates += 1
                if end > start:
                    return False
            if rotates > 1:
                return False
        return True