"""
Level: Hard
Link: https://leetcode.com/problems/count-the-number-of-powerful-integers/
Tags: math, string, dynamic-programming
Description:
You are given three integers start, finish, and limit. You are also given a
0-indexed string s representing a positive integer.

A positive integer x is called powerful if it ends with s (in other words, s is
a suffix of x) and each digit in x is at most limit.

Return the total number of powerful integers in the range [start..finish].

A string x is a suffix of a string y if and only if x is a substring of y that
starts from some index (including 0) in y and extends to the index
y.length - 1. For example, 25 is a suffix of 5125 whereas 512 is not.
"""
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        def get_powerful(num, base, lim):
            if len(num) < len(base):
                return 0
            if len(num) == len(base):
                return 0 if num < base else 1
            valid = 0
            try_len = len(num) - len(base)
            suffix = num[try_len:]
            for try_num in range(try_len):
                if int(num[try_num]) > lim:
                    valid += (lim + 1) ** (try_len - try_num)
                    return valid
                valid += int(num[try_num]) * (lim + 1) ** (try_len - try_num - 1)
            if suffix >= base:
                valid += 1
            return valid

        return get_powerful(str(finish), s, limit) - get_powerful(str(start - 1), s, limit)
