"""
Level: Medium
Link: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
Tags: array, math, dynamic-programming, prefix-sum
Description:
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.
"""
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        total_sum = 0
        odd_count = 0
        zodd = 0
        even_count = 0
        MODULO =  10**9 + 7
        for k in arr:
            total_sum += k
            zodd += ((1 + even_count) if total_sum % 2 else odd_count)
            zodd = zodd % MODULO
            odd_count += total_sum % 2
            even_count += 0 if total_sum % 2 else 1
        return zodd
