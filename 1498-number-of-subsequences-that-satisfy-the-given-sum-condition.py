"""
Level: Medium
Link: https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
Tags: array, two-pointers, binary-search, sorting
Description:
You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the
minimum and maximum element on it is less or equal to target. Since the answer
may be too large, return it modulo 109 + 7.
"""
class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        pows = [1] * len(nums)
        for i in range(1, len(pows)):
            pows[i] = (pows[i - 1] * 2) % MOD
        while l <= r:
            if nums[l] + nums[r] <= target:
                ans = (ans + pows[r - l]) % MOD
                l += 1
            else:
                r -= 1
        return ans