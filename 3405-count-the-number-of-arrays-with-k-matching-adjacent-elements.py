"""
Level: Hard
Link: https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/
Tags: math, combinatorics
Description:
You are given three integers n, m, k. A good array arr of size n is defined as
follows:
 * Each element in arr is in the inclusive range [1, m].
 * Exactly k indices i (where 1 <= i < n) satisfy the condition
   arr[i - 1] == arr[i].

Return the number of good arrays that can be formed.

Since the answer may be very large, return it modulo 109 + 7.
"""
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        facts = [0] * (n + 1)
        inv_facts = [0] * (n + 1)
        def qpow(x, n):
            ans = 1
            while n > 0:
                if n & 1:
                    ans = ans * x % MOD
                x = x * x % MOD
                n >>= 1
            return ans

        facts[0] = 1
        for i in range(1, n + 1):
            facts[i] = facts[i - 1] * i % MOD
        inv_facts[n] = qpow(facts[n], MOD - 2)
        for i in range(n - 1, -1, -1):
            inv_facts[i] = inv_facts[i + 1] * (i + 1) % MOD

        if k >= n:
            return 0
        
        if k < 0 or k > n - 1:
            combos = 0
        else:
            combos = facts[n - 1] * inv_facts[k] % MOD * inv_facts[n - 1 - k] % MOD
        
        values = m * qpow(m - 1, n - 1 - k) % MOD

        return (combos * values) % MOD