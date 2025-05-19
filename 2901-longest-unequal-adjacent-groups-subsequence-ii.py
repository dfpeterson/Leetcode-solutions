"""
Level: Medium
Link: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/
Tags: array, string, dynamic-programming
Description:
You are given a string array words, and an array groups, both arrays having
length n.

The hamming distance between two strings of equal length is the number of
positions at which the corresponding characters are different.

You need to select the longest

from an array of indices [0, 1, ..., n - 1], such that for the subsequence
denoted as [i0, i1, ..., ik-1] having length k, the following holds:
 * For adjacent indices in the subsequence, their corresponding groups are
   unequal, i.e., groups[ij] != groups[ij+1], for each j where 0 < j + 1 < k.
 * words[ij] and words[ij+1] are equal in length, and the hamming distance
   between them is 1, where 0 < j + 1 < k, for all indices in the subsequence.

Return a string array containing the words corresponding to the indices (in
order) in the selected subsequence. If there are multiple answers, return any
of them.

Note: strings in words may be unequal in length.
"""
class Solution:
    def getWordsInLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        ans = []
        N = len(words)
        if not N:
            return ans
        dp = [1] * N
        previous = [-1] * N
        max_len = 1
        end_idx = 0

        for i in range(N):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    if sum([w1 != w2 for w1, w2 in zip(words[i], words[j])]) == 1:
                        if dp[i] < dp[j] + 1:
                            dp[i] = dp[j] + 1
                            previous[i] = j
            if max_len < dp[i]:
                max_len = dp[i]
                end_idx = i
        rsw = []
        curr = end_idx
        while curr != -1:
            rsw.append(words[curr])
            curr = previous[curr]
        return rsw[::-1]