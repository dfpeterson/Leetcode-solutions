"""
Level: Easy
Link: https://leetcode.com/problems/clear-digits/
Tags: string
Description:
For two strings s and t, we say "t divides s" if and only if s = t + t + t +
... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x
divides both str1 and str2.
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if set(list(str1)) != set(list(str2)):
            return ''
        pref = ''
        valid = ''
        for inc in range(1,len(str1)+1):
            pref = str1[:inc]
            if (not str1.replace(pref, '')) and (not str2.replace(pref, '')):
                valid = pref
        return valid