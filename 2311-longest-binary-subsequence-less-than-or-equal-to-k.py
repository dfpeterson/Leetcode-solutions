"""
Level: Medium
Link: https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/
Tags: string, dynamic-programming, greedy, memoization
Description:
You are given a binary string s and a positive integer k.

Return the length of the longest subsequence of s that makes up a binary number
less than or equal to k.

Note:
 * The subsequence can contain leading zeroes.
 * The empty string is considered to be equal to 0.
 * A subsequence is a string that can be derived from another string by
   deleting some or no characters without changing the order of the remaining
   characters.
"""
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        k_s = f'{k:b}' if f'{k:b}' >= s[-len(f'{k:b}'):] else s[-len(f'{k:b}')+1:]
        return min(len(s[:-len(k_s)].replace('1','') + k_s), len(s))