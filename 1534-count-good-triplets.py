"""
Level: Easy
Link: https://leetcode.com/problems/count-good-triplets/
Tags: array, enumeration
Description:
Given an array of integers arr, and three integers a, b and c. You need to find
the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are
true:
 * 0 <= i < j < k < arr.length
 * |arr[i] - arr[j]| <= a
 * |arr[j] - arr[k]| <= b
 * |arr[i] - arr[k]| <= c

Where |x| denotes the absolute value of x.

Return the number of good triplets.
"""
class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        abc = 0
        for m in range(0, len(arr) - 2):
            for n in range(m + 1, len(arr) - 1):
                if abs(arr[m] - arr[n]) <= a:
                    for o in range(n + 1, len(arr)):
                        if abs(arr[n] - arr[o]) <= b and abs(arr[m] - arr[o]) <= c:
                            abc += 1
        return abc