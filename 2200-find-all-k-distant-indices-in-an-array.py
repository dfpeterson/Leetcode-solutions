"""
Level: Easy
Link: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
Tags: array, two-pointers
Description:
You are given a 0-indexed integer array nums and two integers key and k. A
k-distant index is an index i of nums for which there exists at least one index
j such that |i - j| <= k and nums[j] == key.

Return a list of all k-distant indices sorted in increasing order.
"""
class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        ans = []
        l, r = -1, -1
        keys = [i for i in range(len(nums)-1, -1, -1) if nums[i] == key]
        if not keys:
            return ans
        r = keys.pop()
        for j in range(len(nums)):
            if abs(j - r) <= k or (l >= 0 and abs(j - l) <= k):
                ans.append(j)
            if r == j:
                l = r
                r = keys.pop() if keys else float('inf')
        return ans