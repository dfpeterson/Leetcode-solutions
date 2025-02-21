"""
Level: Medium
Link: https://leetcode.com/problems/construct-smallest-number-from-di-string/
Tags: string, backtracking, stack, greedy
Description:
You are given a 0-indexed string pattern of length n consisting of the
characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following
conditions:
 * num consists of the digits '1' to '9', where each digit is used at most
   once.
 * If pattern[i] == 'I', then num[i] < num[i + 1].
 * If pattern[i] == 'D', then num[i] > num[i + 1].

Return the lexicographically smallest possible string num that meets the
conditions.
"""
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        #if it's I insert the number after, if it's D insert it before
        options = list('987654321')
        current = []
        res = []
        for k in range(len(pattern)):
            print(res, current)
            if pattern[k] == 'D':
                current.append(options.pop())
            else:
                res.append(options.pop())
                while current:
                    res.append(current.pop())
        if pattern[-1] == 'D':
            current.append(options.pop())
        else:
            res.append(options.pop())
        while current:
            res.append(current.pop())
        return ''.join(res)