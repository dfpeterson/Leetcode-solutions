"""
Level: Medium
Link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
Tags: hash-table, string, sliding-window
Description:
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these
characters a, b and c.
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        substrings = 0
        p1 = 0
        letters = {l: 0 for l in 'abc'}
        for p2 in range(len(s)):
            letters[s[p2]] += 1
            while all(letters.values()) and p1 <= p2:
                letters[s[p1]] -= 1
                substrings += len(s) - p2
                p1 += 1
        return substrings