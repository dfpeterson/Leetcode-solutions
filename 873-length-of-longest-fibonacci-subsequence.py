"""
Level: Medium
Link: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
Tags: array, hash-table, dynamic-programming
Description:
A sequence x1, x2, ..., xn is Fibonacci-like if:
 * n >= 3
 * xi + xi+1 == xi+2 for all i + 2 <= n

Given a strictly increasing array arr of positive integers forming a sequence,
return the length of the longest Fibonacci-like subsequence of arr. If one
does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of
elements (including none) from arr, without changing the order of the
remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7,
8].
"""
class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        nums_set = set(arr)
        checked_nums = set()
        max_fibo = 0
        def fibo(a, b):
            c = a + b
            fibos = 2
            check = c in nums_set
            while check:
                c = a + b
                checked_nums.add((a, b))
                a, b = b, c
                check = c in nums_set
                fibos += check
            fibos = 0 if fibos == 2 else fibos
            return fibos
        for m, n in enumerate(arr):
            for o in arr[m + 1:]:
                if (n, o) not in checked_nums:
                    max_fibo = max(max_fibo, fibo(n, o))
        return max_fibo
