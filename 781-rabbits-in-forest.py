"""
Level: Medium
Link: https://leetcode.com/problems/rabbits-in-forest/
Tags: array, hash-table, math, greedy
Description:
There is a forest with an unknown number of rabbits. We asked n rabbits "How
many rabbits have the same color as you?" and collected the answers in an
integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in
the forest.
"""
from collections import Counter
from math import ceil
class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        combos = Counter(answers)
        min_rabbits = 0
        for a, c in combos.items():
            b = a + 1
            min_rabbits += ceil(c / b) * b
        return min_rabbits