"""
Level: Easy
Link: https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/
Tags: math, greedy
Description:
You are given an integer num. You know that Bob will sneakily remap one of the
10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by
remapping exactly one digit in num.

Notes:
 * When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences
   of d1 in num with d2.
 * Bob can remap a digit to itself, in which case num does not change.
 * Bob can remap different digits for obtaining minimum and maximum values
   respectively.
 * The resulting number after remapping can contain leading zeroes.
"""
class Solution:
    def minMaxDifference(self, num: int) -> int:
        ans = []
        zero = f'{num}'[0]
        nine = None
        for l in f'{num}':
            if not nine and l != '9':
                nine = l
                break
        ub = int(f'{num}'.replace(nine, '9')) if nine else num
        lb = int(f'{num}'.replace(zero, '0')) if zero else num
        return ub - lb