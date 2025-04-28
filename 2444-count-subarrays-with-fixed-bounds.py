"""
Level: Hard
Link: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
Tags: array, queue, sliding-window, monotonic-queue
Description:
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following
conditions:
 * The minimum value in the subarray is equal to minK.
 * The maximum value in the subarray is equal to maxK.

Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.
"""
class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        last_mink = -1
        last_maxk = -1
        contig_start = -1
        ans = 0
        for k in range(len(nums)):
            if nums[k] == minK:
                last_mink = k
            if nums[k] == maxK:
                last_maxk = k
            if nums[k] < minK or maxK < nums[k]:
                contig_start = k
            ans += max(0, min(last_maxk, last_mink) - contig_start)
        return ans