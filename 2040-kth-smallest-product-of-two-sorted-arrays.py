"""
Level: Hard
Link: http://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays
Tags: array, binary search
Description:
Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer
k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where
0 <= i < nums1.length and 0 <= j < nums2.length. 
"""
from math import ceil
from bisect import bisect_left, bisect_right
class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        def count_prods(val):
            count = 0
            for x in nums1:
                if x > 0:
                    count += bisect_right(nums2, val/x)
                elif x < 0:
                    count += len(nums2) - bisect_left(nums2, ceil(val/x))
                else:
                    if val >= 0:
                        count += len(nums2)
            return count
        low, high = -10**10 - 1, 10**10 + 1
        ans = high
        while low < high:
            mid = (low + high) // 2
            if count_prods(mid) >= k:
                ans = mid
                high = mid
            else:
                low = mid + 1
        return ans
