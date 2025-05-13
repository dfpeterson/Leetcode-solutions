"""
Level: Medium
Link: https://leetcode.com/problems/total-characters-in-string-after-transformations-i/
Tags: hash-table, math, string, dynamic-programming, counting
Description:
You are given a string s and an integer t, representing the number of
transformations to perform. In one transformation, every character in s is
replaced according to the following rules:
 * If the character is 'z', replace it with the string "ab".
 * Otherwise, replace it with the next character in the alphabet. For example,
   'a' is replaced with 'b', 'b' is replaced with 'c', and so on.

Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.
"""
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        chars = [0] * 26
        for c in s:
            chars[ord(c) - 97] += 1
        for _ in range(t//26):
            new_chars = [0] * 26
            for i in range(25):
                new_chars[i] += chars[i]
                new_chars[i + 1] += chars[i]
            new_chars[25] += chars[25]
            new_chars[0] += chars[25]
            new_chars[1] += chars[25]
            chars = [j % MOD for j in new_chars]
        for _ in range(t%26):
            new_chars = [0] * 26
            for i in range(25):
                new_chars[i + 1] += chars[i]
            new_chars[0] += chars[25]
            new_chars[1] += chars[25]
            chars = [j % MOD for j in new_chars]
        return sum(chars) % MOD