"""
Level: Medium
Link: https://leetcode.com/problems/domino-and-tromino-tiling/
Tags: dynamic-programming
Description:
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may
rotate these shapes.

Given an integer n, return the number of ways to tile an 2 x n board. Since the
answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different
if and only if there are two 4-directionally adjacent cells on the board such
that exactly one of the tilings has both squares occupied by a tile.
"""
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        prev1, prev2, prev3 = 5, 2, 1
        current = 0
        k = 4
        if n <= 3:
            return [0, 1, 2, 5][n]
        while k <= n:
            current = ((2 * prev1)  + prev3) % MOD
            prev3 = prev2
            prev2 = prev1
            prev1 = current
            k += 1
        return current
