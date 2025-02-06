"""
Level: Easy
Link: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
Tags: hash-table, string, counting
Description:
You are given two strings s1 and s2 of equal length. A string swap is an
operation where you choose two indices in a string (not necessarily different)
and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most
one string swap on exactly one of the strings. Otherwise, return false.
"""
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if set(s1) != set(s2):
            return False
        swap1, swap2 = None, None
        swap_count = 0
        for a, b in zip(s1, s2):
            if a != b:
                if swap_count == 1:
                    if a != swap2 or b != swap1:
                        return False
                swap_count += 1
                swap1, swap2 = a, b
            if swap_count > 2:
                return False
        if swap_count in (0, 2):
            return True
        else:
            return False
