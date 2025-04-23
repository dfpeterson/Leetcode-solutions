"""
Level: Easy
Link: https://leetcode.com/problems/count-largest-group/
Tags: hash-table, math
Description:
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.
"""
from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        sums = defaultdict(int)
        for d in range(1, n + 1):
            sums[sum(int(e) for e in f'{d}') - 1] += 1
        return sum([e == max(sums.values()) for e in sums.values()])