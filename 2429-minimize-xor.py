"""
Level: Medium
Link: https://leetcode.com/problems/minimize-xor
Tags: greedy, bit-manipulation
Description:
Given two positive integers num1 and num2, find the positive integer x such that:
 * x has the same number of set bits as num2, and
 * The value x XOR num1 is minimal.

Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.
"""
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        if num2.bit_count() == num1.bit_count():
            return num1
        elif num2.bit_count() < num1.bit_count():
            num3 = num1
            mask = 2**num1.bit_length()-1
            point = 1
            while num3.bit_count() > num2.bit_count():
                mask -= point
                num3 = mask & num1
                point = point << 1
            return num3
        else:
            num3 = num1
            shift = 1
            while num3.bit_count() < num2.bit_count():
                num3 = num3 | shift
                shift = shift << 1
            return num3
