"""
Level: Medium
Link: https://leetcode.com/problems/distribute-candies-among-children-ii/
Tags: math, combinatorics, enumeration
Description:
You are given two positive integers n and limit.

Return the total number of ways to distribute n candies among 3 children such
that no child gets more than limit candies.
"""
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def candy_count(candy):
            if candy < 0:
                return 0
            return ((candy + 1) * (candy + 2)) // 2
        ans = candy_count(n)
        ans -= 3 * candy_count(n - limit - 1)
        ans += 3 * candy_count(n - 2 * (limit + 1))
        ans -= candy_count(n - 3 * (limit + 1))
        return ans