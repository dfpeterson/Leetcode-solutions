"""
Level: Esay
Link: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
Tags: array, hash-table, two-pointers
Description:
You are given two 2D integer arrays nums1 and nums2.
 * nums1[i] = [idi, vali] indicate that the number with the id idi has a value
   equal to vali.
 * nums2[i] = [idi, vali] indicate that the number with the id idi has a value
   equal to vali.

Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id,
respecting the following conditions:
 * Only ids that appear in at least one of the two arrays should be included in
   the resulting array.
 * Each id should be included only once and its value should be the sum of the
   values of this id in the two arrays. If the id does not exist in one of the
   two arrays, then assume its value in that array to be 0.

Return the resulting array. The returned array must be sorted in ascending
order by id.
"""
from collections import zip_longest
class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        result_dict = {}
        for n1, n2 in zip_longest(nums1, nums2):
            if n1:
                result_dict[n1[0]] = result_dict.get(n1[0], 0) + n1[1]
            if n2:
                result_dict[n2[0]] = result_dict.get(n2[0], 0) + n2[1]
        return [[a, result_dict[a]] for a in sorted(result_dict)]