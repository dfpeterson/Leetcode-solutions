"""
Level: Easy
Link: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
Tags: array, hash-table, counting
Description:
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to
dominoes[j] = [c, d] if and only if either (a == c and b == d), or
(a == d and b == c) - that is, one domino can be rotated to be equal to another
domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and
dominoes[i] is equivalent to dominoes[j].
"""
from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        ans = 0
        bones = defaultdict(int)
        for domino in dominoes:
            ans += bones[(min(domino), max(domino))]
            bones[(min(domino), max(domino))] += 1
        return ans