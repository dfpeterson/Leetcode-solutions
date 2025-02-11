"""
Level: Medium
Link: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
Tags: string, stack, simulation
Description:
Given two strings s and part, perform the following operation on s until all
occurrences of the substring part are removed:
 * Find the leftmost occurrence of the substring part and remove it from s.

Return s after removing all occurrences of part.
"""
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Generate a list as a stack, if the stack ends in part, pop len(part)
        string_stack = []
        compare = list(part)
        for letter in s:
            string_stack.append(letter)
            if string_stack[-len(part):] == compare:
                for magnitude in part:
                    string_stack.pop()
        return ''.join(string_stack)