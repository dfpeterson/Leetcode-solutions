"""
Level: Medium
Link: https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
Tags: math
Description:
Given an integer n, return true if it is possible to represent n as the sum of
distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that
y == 3x.
"""
from math import ceil, log
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        cubes = [3**n for n in range(ceil(log(n,3)+1))]
        for c in reversed(cubes):
            n -= c if c <= n else 0
        return n == 0