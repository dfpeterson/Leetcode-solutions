"""
Level: Hard
Link: https://leetcode.com/problems/count-the-number-of-ideal-arrays/
Tags: math, dynamic-programming, combinatorics, number-theory
Description:
You are given two integers n and maxValue, which are used to describe an ideal
array.

A 0-indexed integer array arr of length n is considered ideal if the following
conditions hold:
 * Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
 * Every arr[i] is divisible by arr[i - 1], for 0 < i < n.

Return the number of distinct ideal arrays of length n. Since the answer may be
very large, return it modulo 109 + 7.
"""
from math import comb
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        permutes = {}
        def childArrays(cur_max, max_pos):
            ans = 0
            if (cur_max, max_pos) in permutes:
                return permutes[(cur_max, max_pos)]
            ans = comb(n - 1, max_pos - 1)
            n_pos = cur_max + cur_max
            if max_pos == n or n_pos > maxValue:
                return ans
            while n_pos <= maxValue:
                ans = (ans + childArrays(n_pos, max_pos + 1)) % MOD
                n_pos += cur_max
            permutes[(cur_max, max_pos)] = ans
            return ans
        return sum([childArrays(i, 1) for i in range(1, maxValue + 1)]) % MOD
