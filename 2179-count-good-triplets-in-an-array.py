"""
Level: Hard
Link: https://leetcode.com/problems/count-good-triplets-in-an-array/
Tags: array, binary-search, divide-and-conquer, binary-indexed-tree, segment-tree, merge-sort, ordered-set, set, binary-search-tree, binary-tree
Description:
You are given two 0-indexed arrays nums1 and nums2 of length n, both of which
are permutations of [0, 1, ..., n - 1].

A good triplet is a set of 3 distinct values which are present in increasing
order by position both in nums1 and nums2. In other words, if we consider pos1v
as the index of the value v in nums1 and pos2v as the index of the value v in
nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1,
such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.

Return the total number of good triplets.
"""
from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        appeared1 = [None] * N
        appeared2 = []
        tracked = SortedList()
        goodgoodnums = 0
        for i, n1 in enumerate(nums1):
            appeared1[n1] = i
        for n2 in nums2:
            appeared2.append(appeared1[n2])
        for x in appeared2:
            left = len(tracked)
            smaller_left = tracked.bisect_left(x)
            right = N - 1 - left
            bigger = N - 1 - x
            bigger_left = left - smaller_left
            bigger_right = bigger - bigger_left
            goodgoodnums += smaller_left * bigger_right
            tracked.add(x)
        return goodgoodnums