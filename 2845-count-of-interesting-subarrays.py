"""
Level: Medium
Link: https://leetcode.com/problems/count-complete-subarrays-in-an-array/
Tags: array, hash-table, prefix-sum
Description:
You are given a 0-indexed integer array nums, an integer modulo, and an
integer k.

Your task is to find the count of subarrays that are interesting.

A subarray nums[l..r] is interesting if the following condition holds:
 * Let cnt be the number of indices i in the range [l, r] such that
   nums[i] % modulo == k. Then, cnt % modulo == k.

Return an integer denoting the count of interesting subarrays.

Note: A subarray is a contiguous non-empty sequence of elements within an
array.
"""
from collections import defaultdict
class Solution:
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        ans = 0
        mod_prefixes = defaultdict(int)
        mod_sum = 0
        for a_num in nums:
            mod_sum += a_num % modulo == k
            ans += ((mod_sum % modulo) == k) +  mod_prefixes[(modulo + mod_sum - k) % modulo]
            mod_prefixes[(mod_sum % modulo)] += 1
        return ans