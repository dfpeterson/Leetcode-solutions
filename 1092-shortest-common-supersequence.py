"""
Level: Hard
Link: https://leetcode.com/problems/shortest-common-supersequence/
Tags: string, dynamic-programming
Description:
Given two strings str1 and str2, return the shortest string that has both str1
and str2 as subsequences. If there are multiple valid strings, return any of
them.

A string s is a subsequence of string t if deleting some number of characters
from t (possibly 0) results in the string s.
"""
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        previous = [str2[j:] for j in range(len(str2))]
        previous.append('')
        if str1 == str2:
            return str1
        for s1 in range(len(str1) - 1, -1, -1):
            current = [''] * len(str2)
            current.append(str1[s1:])
            for s2 in range(len(str2) - 1, -1, -1):
                if str1[s1] == str2[s2]:
                    current[s2] = str1[s1] + previous[s2 + 1]
                else:
                    r1 = str1[s1] + previous[s2]
                    r2 = str2[s2] + current[s2 + 1]
                    current[s2] = r1 if len(r1) < len(r2) else r2
            previous = current
        return current[0]