"""
Level: Medium
Link: https://leetcode.com/problems/maximum-erasure-value/
Tags: array, hash-table, sliding-window
Description:
You are given an array of positive integers nums and want to erase a subarray
containing unique elements. The score you get by erasing the subarray is equal
to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence
of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
"""
class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        l = 0
        ans = 0
        check = set()
        window_sum = 0
        for r in range(len(nums)):
            while nums[r] in check:
                window_sum -= nums[l]
                check.remove(nums[l])
                l += 1
            check.add(nums[r])
            window_sum += nums[r]
            ans = max(ans, window_sum)
        return ans