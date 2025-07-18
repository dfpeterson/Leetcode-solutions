"""
Level: Medium
Link: https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/
Tags: array, dynamic-programming
Description:
You are given an integer array nums and a positive integer k.

A subsequence sub of nums with length x is called valid if it satisfies:
 * (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] +
   sub[x - 1]) % k.

Return the length of the longest valid subsequence of nums. 
"""
class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        ks = [[0] * k for _ in range(k)]
        ans = 0
        for num in nums:
            num %= k
            for prev in range(k):
                ks[num][prev] = ks[prev][num] + 1
            ans = max(ans, max(ks[num]))
        return ans
