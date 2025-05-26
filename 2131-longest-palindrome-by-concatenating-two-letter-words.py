"""
Level: Medium
Link: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
Tags: array, hash-table, string, greedy, counting
Description:
You are given an array of strings words. Each element of words consists of two
lowercase English letters.

Create the longest possible palindrome by selecting some elements from words
and concatenating them in any order. Each element can be selected at most
once.

Return the length of the longest palindrome that you can create. If it is
impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.
"""
from collections import Counter
class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        pal_bits = Counter(words)
        reflexed = False
        used = set()
        ans = 0
        for pal_bit in pal_bits:
            if pal_bit in used:
                continue
            if pal_bit == pal_bit[::-1]:
                if reflexed:
                    ans += (pal_bits[pal_bit]//2) * 4
                else:
                    ans += pal_bits[pal_bit] * 2
            else:
                ans += min(pal_bits[pal_bit], pal_bits[pal_bit[::-1]]) * 4
            used |= {pal_bit, pal_bit[::-1]}
            if pal_bit == pal_bit[::-1] and pal_bits[pal_bit] % 2 == 1 and not reflexed:
                reflexed = True
        return ans

