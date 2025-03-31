"""
Level: Medium
Link: https://leetcode.com/problems/partition-labels/
Tags: hash-table, two-pointers, string, greedy
Description:
You are given a string s. We want to partition the string into as many parts as
possible so that each letter appears in at most one part. For example,
the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such
as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in
order, the resultant string should be s.

Return a list of integers representing the size of these parts.
"""
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        letters = {}
        letter_ord = []
        for pos, letter in enumerate(s):
            if letter in letters:
                letters[letter][1] = pos
            else:
                letters[letter] = [pos, pos]
                letter_ord.append(letter)
        l, r = 0, 0
        lengths = []
        for letter in letter_ord:
            if letters[letter][0] > r:
                lengths.append(r - l + 1)
                l, r = letters[letter]
            elif letters[letter][1] > r:
                r = letters[letter][1]
        lengths.append(r - l + 1)
        return lengths