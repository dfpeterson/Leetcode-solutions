"""
Level: Easy
Link: https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/
Tags: array, hash-table
Description:
You are given an integer array nums. You need to ensure that the elements in
the array are distinct. To achieve this, you can perform the following
operation any number of times:
 * Remove 3 elements from the beginning of the array. If the array has fewer
   than 3 elements, remove all remaining elements.

Note that an empty array is considered to have distinct elements. Return the
minimum number of operations needed to make the elements in the array distinct.
"""
from math import ceil
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        og_nums = len(nums)
        if og_nums == len(set(nums)):
            return 0
        distincts = set()
        p = og_nums - 1
        while p > 0:
            if nums[p] in distincts:
                p = 0
            else:
                distincts.add(nums[p])
                p -= 1
        return int(ceil((og_nums - len(distincts))/3))