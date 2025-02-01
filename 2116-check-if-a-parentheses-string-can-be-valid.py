"""
Level: Medium
Link: https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/
Tags: string, stack, greedy
Description:
A parentheses string is a non-empty string consisting only of '(' and ')'. It
is valid if any of the following conditions is true:
 * It is ().
 * It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
 * It can be written as (A), where A is a valid parentheses string.

You are given a parentheses string s and a string locked, both of length n.
locked is a binary string consisting only of '0's and '1's. For each index i of
locked,
 * If locked[i] is '1', you cannot change s[i].
 * But if locked[i] is '0', you can change s[i] to either '(' or ')'.

Return true if you can make s a valid parentheses string. Otherwise, return
false.
"""
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        #count 0s and )s going right and then 0s and (s going left
        if len(s) % 2 == 1 or (s[0] == ')' and locked[0] == '1') or (s[-1] == '(' and locked[-1] == '1'):
            return False
        #print(so, sc)
        opened = 0
        buff = 0
        for paren, stat in zip(s, locked):
            if stat == '0':
                buff += 1
            elif paren == '(':
                opened += 1
            else:
                if opened > 0:
                    opened -= 1
                else:
                    buff -= 1
            if buff < 0:
                return False
        closed = 0
        buff = 0
        for paren, stat in zip(reversed(s), reversed(locked)):
            if stat == '0':
                buff += 1
            elif paren == ')':
                closed += 1
            else:
                if closed > 0:
                    closed -= 1
                else:
                    buff -= 1
            if buff < 0:
                return False
        return True
