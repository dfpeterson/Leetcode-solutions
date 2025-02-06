"""
Level: Medium
Link: https://leetcode.com/problems/tuple-with-same-product/
Tags: array, hash-table, counting
Description:
Given an array nums of distinct positive integers, return the number of tuples
(a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums,
and a != b != c != d.
"""
class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        answers = {}
        counts = 0
        for x, a in enumerate(nums):
            for b in nums[x:]:
                if a != b:
                    if a * b in answers:
                        if (a, b) not in answers[a * b] and (b, a) not in answers[a * b]:
                            counts += len(answers[a*b])*4
                            answers[a * b] = answers[a * b] | {(a, b), (b, a)}
                    else:
                        answers[a * b] = {(a, b), (b, a)}
        return counts