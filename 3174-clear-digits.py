"""
Level: Easy
Link: https://leetcode.com/problems/clear-digits/
Tags: string, stack, simulation
Description:
You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:
 * Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.
"""
class Solution:
    def clearDigits(self, s: str) -> str:
        string_stack = []
        pop_deficit = 0
        for char in s:
            if char.isdigit() and string_stack:
                string_stack.pop()
            else:
                string_stack.append(char)
        return "".join(string_stack)
