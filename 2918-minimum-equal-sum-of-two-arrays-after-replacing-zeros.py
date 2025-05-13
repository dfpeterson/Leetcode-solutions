"""
Level: Medium
Link: https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
Tags: array, greedy
Description:
You are given two arrays nums1 and nums2 consisting of positive integers.

You have to replace all the 0's in both arrays with strictly positive integers
such that the sum of elements of both arrays becomes equal.

Return the minimum equal sum you can obtain, or -1 if it is impossible.
"""
class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if (not zeros1 and (sum1 < (sum2 + zeros2))) or (not zeros2 and (sum2 < (sum1 + zeros1))):
            return -1
        return max(sum1 + zeros1, sum2 + zeros2)