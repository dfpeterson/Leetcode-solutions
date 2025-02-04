"""
Level: Medium
Link: https://leetcode.com/problems/reverse-integer/
Tags: math
Description:
Given a signed 32-bit integer x, return x with its digits reversed. If
reversing x causes the value to go outside the signed 32-bit integer range
[-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or
unsigned).
"""
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return int(f'{abs(x)}'[::-1])*-1 if int(f'{abs(x)}'[::-1])*-1 >= -2**31 else 0
        else:
            return int(f'{x}'[::-1]) if int(f'{x}'[::-1]) <= 2**31 - 1 else 0