"""
Level: Easy
Link: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency/
Tags: hash-table, string, counting
Description:
You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = freq(a1) - freq(a2) between
the frequency of characters a1 and a2 in the string such that:
 * a1 has an odd frequency in the string.
 * a2 has an even frequency in the string.

Return this maximum difference.
"""
from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        letters = Counter(s)
        odd = 0
        even = float('inf')
        for letter in letters.values():
            if letter % 2:
                odd = max(odd, letter)
            else:
                even = min(even, letter)
        return odd - even