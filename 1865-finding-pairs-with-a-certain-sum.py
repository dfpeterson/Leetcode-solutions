"""
Level: Medium
Link: https://leetcode.com/problems/finding-pairs-with-a-certain-sum/
Tags: array, hash-table, design
Description:
You are given two integer arrays nums1 and nums2. You are tasked to implement a
data structure that supports queries of two types:
 * Add a positive integer to an element of a given index in the array nums2.
 * Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a
   given value (0 <= i < nums1.length and 0 <= j < nums2.length).

Implement the FindSumPairs class:
 * FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object
   with two integer arrays nums1 and nums2.
 * void add(int index, int val) Adds val to nums2[index], i.e., apply
   nums2[index] += val.
 * int count(int tot) Returns the number of pairs (i, j) such that
   nums1[i] + nums2[j] == tot.
"""
from collections import Counter
class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.n1 = nums1
        self.n2 = nums2
        self.nc1 = Counter(self.n1)
        self.nc2 = Counter(self.n2)

    def add(self, index: int, val: int) -> None:
        self.n2[index] += val
        self.nc2[self.n2[index] - val] -= 1
        self.nc2[self.n2[index]] += 1


    def count(self, tot: int) -> int:
        ans = 0
        for i in self.nc1:
            if tot - i in self.nc2:
                ans += self.nc1[i] * self.nc2[tot - i]
        return ans