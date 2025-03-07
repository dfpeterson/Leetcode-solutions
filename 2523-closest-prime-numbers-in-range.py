"""
Level: Medium
Link: https://leetcode.com/problems/closest-prime-numbers-in-range/
Tags: math, number-theory
Description:
Given two positive integers left and right, find the two integers num1 and num2
such that:
 * left <= num1 < num2 <= right .
 * Both num1 and num2 are prime numbers.
 * num2 - num1 is the minimum amongst all other pairs satisfying the above
   conditions.

Return the positive integer array ans = [num1, num2]. If there are multiple
pairs satisfying these conditions, return the one with the smallest num1 value.
If no such numbers exist, return [-1, -1].
"""
class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        prime_check = [False, False] + ([True] * right)
        for k in range(2, int(right**.5)+1):
            if prime_check[k]:
                for l in range(2 * k, right + 1, k):
                    prime_check[l] = False
        dist = right - left + 1
        a, b = -1, -1
        s1 = float('-inf')
        for num in range(left, right + 1):
            if prime_check[num]:
                if num - s1 < dist:
                    a, b = s1, num
                    dist = num - s1
                s1 = num
        return [a, b]