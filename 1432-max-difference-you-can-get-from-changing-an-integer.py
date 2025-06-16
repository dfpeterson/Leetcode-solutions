"""
Level: Medium
Link: https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
Tags: math, greedy
Description:
You are given an integer num. You will apply the following steps to num two
separate times:
 * Pick a digit x (0 <= x <= 9).
 * Pick another digit y (0 <= y <= 9). Note y can be equal to x.
 * Replace all the occurrences of x in the decimal representation of num by y.

Let a and b be the two results from applying the operation to num
independently.

Return the max difference between a and b.

Note that neither a nor b may have any leading zeros, and must not be 0.
"""
class Solution:
    def maxDiff(self, num: int) -> int:
        numstr = f'{num}'
        ub = None if numstr[0] == '9' else numstr[0]
        lb = None if numstr[0] == '1' else numstr[0]
        for n in numstr:
            if not ub and n != '9':
                ub = n
            if not lb and n != '0' and n != '1':
                lb = n
            if lb and ub:
                break
        maxnum = int(numstr.replace(ub, '9')) if ub else num
        minnum = int(numstr.replace(lb, '1' if lb == numstr[0] else '0')) if lb else num
        return maxnum - minnum