"""
Level: Medium
Link: https://leetcode.com/problems/find-the-punishment-number-of-an-integer/
Tags: math, backtracking
Description:
Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers
i such that:
 *  1 <= i <= n
 * The decimal representation of i * i can be partitioned into contiguous
   substrings such that the sum of the integer values of these substrings
   equals i.
"""
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def slice_and_dice(ind: int, cur: int, ans: int, strans: str) -> bool:
            if ind == len(strans) and cur == ans:
                return True
            for k in range(ind, len(strans)):
                if slice_and_dice(k + 1, cur + int(strans[ind:k+1]), ans, strans):
                    return True
            return False

        ans = 0
        for m in range(1, n+1):
            if m % 9 in (0, 1):
                if slice_and_dice(0, 0, m, str(m*m)):
                    print(f'm: {m}')
                    ans += m * m
        return ans
