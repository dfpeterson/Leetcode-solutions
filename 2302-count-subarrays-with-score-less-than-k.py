"""
Level: Hard
Link: https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
Tags: array, binary-search, sliding-window, prefix-sum
Description:
The score of an array is defined as the product of its sum and its length.
 * For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.

Given a positive integer array nums and an integer k, return the number of
non-empty subarrays of nums whose score is strictly less than k.

A subarray is a contiguous sequence of elements within an array.
"""
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        N = len(nums)
        p1, p2 = 0, 0
        current_score = 0
        ans = 0
        while p2 < N:
            current_score += nums[p2]
            while current_score * (p2 - p1 + 1) >= k:
                current_score -= nums[p1]
                p1 += 1
            ans += p2 - p1 + 1
            p2 += 1
        return ans