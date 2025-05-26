"""
Level: Medium
Link: https://leetcode.com/problems/zero-array-transformation-i/
Tags: array, prefix-sum
Description:
You are given an integer array nums of length n and a 2D array queries, where
queries[i] = [li, ri].

For each queries[i]:
 * Select a subset of indices within the range [li, ri] in nums.
 * Decrement the values at the selected indices by 1.

A Zero Array is an array where all elements are equal to 0.

Return true if it is possible to transform nums into a Zero Array after
processing all the queries sequentially, otherwise return false.
"""
class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        da = [0] * (len(nums) + 1)
        for query in queries:
            l, r = query
            da[l] += 1
            da[r+1] -= 1
        delta_sum = 0
        for i in range(len(nums)):
            delta_sum += da[i]
            if delta_sum < nums[i]:
                return False
        return True