"""
Level: Hard
Link: https://leetcode.com/problems/longest-subsequence-repeated-k-times
Tags: string, backtracking, greedy, counting, enumeration
Description: 
You are given a string s of length n, and an integer k. You are tasked to find
the longest subsequence repeated k times in string s.

A subsequence is a string that can be derived from another string by deleting
some or no characters without changing the order of the remaining characters.

A subsequence seq is repeated k times in the string s if seq * k is a
subsequence of s, where seq * k represents a string constructed by
concatenating seq k times.
 * For example, "bba" is repeated 2 times in the string "bababcba", because the
   string "bbabba", constructed by concatenating "bba" 2 times, is a
   subsequence of the string "bababcba".

Return the longest subsequence repeated k times in string s. If multiple such
subsequences are found, return the lexicographically largest one. If there is
no such subsequence, return an empty string.
"""
from collections import Counter, deque
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def lookahead(sub):
            target = sub * k
            siter = iter(s)
            return all(c in siter for c in target)

        letter_counts = Counter(s)
        chars = sorted([char for char, count in letter_counts.most_common() if count >= k],reverse=True)
        ans = ''
        q = deque([''])
        while q:
            curr_char = q.popleft()
            for char in chars:
                next_char = curr_char + char
                if lookahead(next_char):
                    if len(next_char) > len(ans):
                        ans = next_char
                    q.append(next_char)
        return ans
