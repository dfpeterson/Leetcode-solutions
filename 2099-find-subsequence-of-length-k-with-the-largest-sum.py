"""
Level: Easy
Link: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
Tags: array, hash-table, sorting, heap-priority-queue
Description: 
You are given an integer array nums and an integer k. You want to find a
subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.
"""
class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        numss = sorted([(num, pos) for pos, num in enumerate(nums)], reverse=True)
        return [n[0] for n in sorted(numss[:k], key=lambda x: x[1])]