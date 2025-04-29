"""
Level: Medium
Link: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
Tags: array, sliding-window
Description:
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at
least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.
"""
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        lk = 0
        ks = 0
        max_ele = max(nums)
        ans = 0
        for r in range(len(nums)):
            if nums[r] == max_ele:
                ks += 1
            while ks >= k:
                if nums[lk] == max_ele:
                    ks -= 1
                lk += 1
            ans += lk
        return ans