"""
Level: Medium
Link: https://leetcode.com/problems/product-of-array-except-self/
Tags: array, prefix sum
Description:
Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zero_count = 0
        prod_sum = 1
        for b in nums:
            if b == 0:
                zero_count += 1
            else:
                prod_sum *= b
        if zero_count > 1:
            prod_sum = 0
        return [int((prod_sum/a) if not zero_count else 0) if a else prod_sum for a in nums]