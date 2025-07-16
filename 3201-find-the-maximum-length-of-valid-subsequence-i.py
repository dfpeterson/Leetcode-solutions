"""
Level: Medium
Link: https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/
Tags: array, dynamic-programming
Description:
You are given an integer array nums.

A subsequence sub of nums with length x is called valid if it satisfies:
 * (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.

Return the length of the longest valid subsequence of nums.
"""
class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        nums = [num % 2 for num in nums]
        odd_check = sum(nums)
        ans = max(odd_check, len(nums) - odd_check)
        odd_s, even_s = 0, 0
        odd_t, even_t = None, None
        for n in nums:
            if odd_t == None and n:
                odd_t = n
                odd_s = 1
            elif even_t == None and n == 0:
                even_t = 0
                even_s = 1
            if n != odd_t:
                odd_t = n
                odd_s += 1
            elif n != even_t:
                even_t = n
                even_s += 1
        return max(ans, even_s, odd_s)