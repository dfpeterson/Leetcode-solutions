"""
Level: Medium
Link: https://leetcode.com/problems/maximum-score-from-removing-substrings/
Tags: string, stack, greedy
Description:
You are given a string s and two integers x and y. You can perform two types of
operations any number of times.
 * Remove substring "ab" and gain x points.
   * For example, when removing "ab" from "cabxbae" it becomes "cxbae".
 * Remove substring "ba" and gain y points.
   * For example, when removing "ba" from "cabxbae" it becomes "cabxe".

Return the maximum points you can gain after applying the above operations on
s.
"""
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        stack = []
        if y > x:
            top = ('ba', y)
            bot = ('ab', x)
        else:
            top = ('ab', x)
            bot = ('ba', y)
        for c in s:
            if c == top[0][1] and stack and stack[-1] == top[0][0]:
                ans += top[1]
                stack.pop()
            else:
                stack.append(c)
        s = ''.join(stack)
        stack = []
        for c in s:
            if c == bot[0][1] and stack and stack[-1] == bot[0][0]:
                ans += bot[1]
                stack.pop()
            else:
                stack.append(c)
        return ans