"""
Level: Medium  
Link: https://leetcode.com/problems/minimum-length-of-string-after-operations/
Tags: hash-table, string, counting
Description: 
You are given a string s.

You can perform the following process on s any number of times:
 * Choose an index i in the string such that there is at least one character to
   the left of index i that is equal to s[i], and at least one character to the
   right that is also equal to s[i].
 * Delete the closest character to the left of index i that is equal to s[i].
 * Delete the closest character to the right of index i that is equal to s[i].

Return the minimum length of the final string s that you can achieve.
"""
class Solution:
    def minimumLength(self, s: str) -> int:
        chars = {}
        for char in s:
            if chars.get(char,0)>=2:
                chars[char] -= 1
            else:
                chars[char] = chars.get(char,0) + 1
        return sum(chars.values())