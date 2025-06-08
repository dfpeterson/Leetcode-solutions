"""
Level: Medium
Link: https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/
Tags: hash-table, string, stack, greedy, heap-priority-queue
Description:
You are given a string s. It may contain any number of '*' characters. Your
task is to remove all '*' characters.

While there is a '*', do the following operation:
 * Delete the leftmost '*' and the smallest non-'*' character to its left. If
   there are several smallest characters, you can delete any of them.

Return the lexicographically smallest resulting string after removing all '*'
characters.
"""
import heapq
class Solution:
    def clearStars(self, s: str) -> str:
        heapy = []
        ans = [''] * len(s)
        heapq.heapify(heapy)
        for p in range(len(s)):
            if s[p] == '*':
                heapq.heappop(heapy)
            else:
                heapq.heappush(heapy, (s[p], -1*p))
        while heapy:
            c, i = heapq.heappop(heapy)
            ans[-1*i] = c
        return ''.join(ans)