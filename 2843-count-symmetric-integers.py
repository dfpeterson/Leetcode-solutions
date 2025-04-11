"""
Level: Easy
Link: https://leetcode.com/problems/count-symmetric-integers/
Tags: math, enumeration
Description:
You are given two positive integers low and high.

An integer x consisting of 2 * n digits is symmetric if the sum of the first n
digits of x is equal to the sum of the last n digits of x. Numbers with an odd
number of digits are never symmetric.

Return the number of symmetric integers in the range [low, high].
"""
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symetrics = (min(high, 100)//11) - (min(low-1,100)//11)
        if high < 1000:
            return symetrics
        for k in range(max(1000, low), min(10000, high + 1)):
            if (k//1000) + ((k % 1000) // 100) == ((k % 100) // 10) + (k % 10):
                symetrics += 1
        return symetrics