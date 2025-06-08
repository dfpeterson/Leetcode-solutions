"""
Level: Medium
Link: https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/
Tags: hash-table, string, stack, greedy
Description:
You are given a string s and a robot that currently holds an empty string t.
Apply one of the following operations until s and t are both empty:
 * Remove the first character of a string s and give it to the robot. The robot
   will append this character to the string t.
 * Remove the last character of a string t and give it to the robot. The robot
   will write this character on paper.

Return the lexicographically smallest string that can be written on the paper.
"""
class Solution:
    def robotWithString(self, s: str) -> str:
        char_count = [0] * 26
        for c in s:
            char_count[ord(c) - 97] += 1
        
        min_char = ord(min(s))

        t = []
        p = []

        for c in s:
            t.append(c)
            char_count[ord(c) - 97] -= 1

            while min_char <= 122 and char_count[min_char - 97] == 0:
                min_char += 1

            comp_char = chr(min_char) if min_char <= 122 else '{'

            while t and t[-1] <= comp_char:
                p.append(t.pop())

        while t:
            p.append(t.pop())

        return ''.join(p)