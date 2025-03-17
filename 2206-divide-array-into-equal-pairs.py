"""
Level: Easy
Link: https://leetcode.com/problems/divide-array-into-equal-pairs/
Tags: array, hash-table, bit-manipulation, counting
Description:
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

    Each element belongs to exactly one pair.
    The elements present in a pair are equal.

Return true if nums can be divided into n pairs, otherwise return false.
"""
class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        numcount = {}
        for n in nums:
            numcount[n] = (numcount.get(n, 0) + 1) % 2
        return not any(numcount.values())