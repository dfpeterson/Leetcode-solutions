"""
Level: Medium
Link: https://leetcode.com/problems/zero-array-transformation-ii/
Tags: array, binary-search, prefix-sum
Description:
You are given an integer array nums of length n and a 2D array queries where
queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:
 * Decrement the value at each index in the range [li, ri] in nums by at most
   vali.
 * The amount by which each value is decremented can be chosen independently
   for each index.

A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing
the first k queries in sequence, nums becomes a Zero Array. If no such k
exists, return -1.
"""
class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        def bs(check):
            diff_arr = [0] * (len(nums) + 1)
            for query in queries[:check]:
                diff_arr[query[0]] += query[2]
                diff_arr[query[1]+1] -= query[2]
            for i in range(1, len(nums) + 1):
                diff_arr[i] += diff_arr[i - 1]
            for num, diff in zip(nums, diff_arr):
                if num > diff:
                    return False
            return True
        p1, p2 = 0, len(queries) + 1
        while p1 < p2:
            mp = (p1 + p2) // 2
            if bs(mp):
                p2 = mp
            else:
                p1 = mp + 1
        if p1 == len(queries) + 1:
            return -1
        return p1