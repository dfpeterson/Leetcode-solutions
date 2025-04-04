"""
Level: Easy
Link: https://leetcode.com/problems/clear-digits/
Tags: two-pointers, string
Description:
You are given two strings word1 and word2. Merge the strings by adding letters
in alternating order, starting with word1. If a string is longer than the
other, append the additional letters onto the end of the merged string.

Return the merged string.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join([f'{word1[k] if k < len(word1) else ""}{word2[k] if k < len(word2) else ""}' for k in range(max(len(word1), len(word2)))])