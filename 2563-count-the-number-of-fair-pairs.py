"""
Level: Medium
Link: https://leetcode.com/problems/count-and-say/
Tags: array, two-pointers, binary-search, sorting
Description:
Given a 0-indexed integer array nums of size n and two integers lower and
upper, return the number of fair pairs.

A pair (i, j) is fair if:
 * 0 <= i < j < n, and
 * lower <= nums[i] + nums[j] <= upper
"""
class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        def get_pairs(bound):
            lb = 0
            ub = len(nums) - 1
            pairs = 0
            while lb < ub:
                if nums[lb] + nums[ub] <= bound:
                    pairs += ub - lb
                    lb += 1
                else:
                    ub -= 1
            return pairs
        return get_pairs(upper) - get_pairs(lower - 1)