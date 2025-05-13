"""
Level: Hard
Link: https://leetcode.com/problems/count-number-of-balanced-permutations/
Tags: math, string, dynamic-programming, combinatorics
Description:
You are given a string num. A string of digits is called balanced if the sum of
the digits at even indices is equal to the sum of the digits at odd indices.

Return the number of distinct permutations of num that are balanced.

Since the answer may be very large, return it modulo 109 + 7.

A permutation is a rearrangement of all the characters of a string.
"""
from functools import lru_cache
from math import comb
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        target_sum = sum([int(k) for k in num])
        if target_sum % 2:
            return 0
        num_len = len(num)
        counts = [0] * 10
        for n in num:
            counts[int(n)] += 1
        factorial = [1] * (num_len + 1)
        inv_factorial = [1] * (num_len + 1)
        for i in range(1, num_len + 1):
            factorial[i] = factorial[i - 1] * i % MOD
        inv_factorial[num_len] = pow(factorial[num_len], MOD - 2, MOD)
        for j in range(num_len - 1, -1, -1):
            inv_factorial[j] = inv_factorial[j + 1] * (j + 1) % MOD

        @lru_cache(maxsize=None)
        def dfs(i, j, a, b):
            if i == 10:
                return int(j == 0 and a == 0 and b == 0)
            ans = 0
            for l in range(min(counts[i], a) + 1):
                r = counts[i] - l
                if r > b or l * i > j:
                    continue
                ways = comb(a, l) * comb(b, r) % MOD
                ans += ways * dfs(i + 1, j - l * i, a - l, b - r)
                ans = ans % MOD
            return ans
        return dfs(0, target_sum//2, num_len // 2, (num_len + 1)//2)
