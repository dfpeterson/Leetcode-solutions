"""
Level: Medium
Link: https://leetcode.com/problems/bitwise-xor-of-all-pairings/
Tags: array, bit-manipulation
Description:
You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative
integers. There exists another array, nums3, which contains the bitwise XOR of
all pairings of integers between nums1 and nums2 (every integer in nums1 is
paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3.
"""
class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        num1reduce = 0
        num2reduce = 0
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0
        if len(nums2) % 2 == 1:
            for a in nums1:
                num1reduce = num1reduce ^ a
        if len(nums1) % 2 == 1:
            for b in nums2:
                num2reduce = num2reduce ^ b
        return num1reduce ^ num2reduce
