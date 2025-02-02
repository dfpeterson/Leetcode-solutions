"""
Level: Medium
Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
Tags: array, hash-table, bit-manipulation
Description:
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the
count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers
from 1 to n exactly once.
"""
class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        results = []
        prev = 0
        for k in range(len(A)):
            prev += A[:k].count(B[k]) + B[:k].count(A[k]) + (A[k] == B[k])
            results.append(prev)
        return results