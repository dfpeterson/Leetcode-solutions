"""
Level: Medium
Link: https://leetcode.com/problems/count-good-numbers/
Tags: math, recursion
Description:
A digit string is good if the digits (0-indexed) at even indices are even and
the digits at odd indices are prime (2, 3, 5, or 7).
 * For example, "2582" is good because the digits (2 and 8) at even positions
   are even and the digits (5 and 2) at odd positions are prime. However,
   "3245" is not good because 3 is at an even index but is not even.

Given an integer n, return the total number of good digit strings of length n.
Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain
leading zeros.
"""
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even = n // 2 + n % 2
        odd = n // 2
        def kapow(base, xpow):
            result = 1
            while xpow > 0:
                if xpow % 2:
                    result = (result * base) % MOD
                xpow = xpow // 2
                base = (base ** 2) % MOD
            return result

        return (kapow(5, even) * kapow(4, odd)) % MOD