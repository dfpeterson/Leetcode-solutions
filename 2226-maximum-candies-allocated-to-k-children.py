"""
Level: Medium
Link: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/
Tags: array, binary-search
Description:
You are given a 0-indexed integer array candies. Each element in the array
denotes a pile of candies of size candies[i]. You can divide each pile into any
number of sub piles, but you cannot merge two piles together.

You are also given an integer k. You should allocate piles of candies to k
children such that each child gets the same number of candies. Each child can
be allocated candies from only one pile of candies and some piles of candies
may go unused.

Return the maximum number of candies each child can get.
"""
class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        # this is a reverse divisor
        # answer is sum candies // z == k
        # start min candies and bin search backward
        left_pile, right_pile = 1, sum(candies)//k
        amt = 0
        if not right_pile:
            return 0
        def divide_candies(n):
            return sum([pile // n for pile in candies if pile >= n])

        while left_pile <= right_pile:
            mid_pile = (left_pile + right_pile) // 2
            pile_count = divide_candies(mid_pile)
            if pile_count < k:
                right_pile = mid_pile - 1
            else:
                amt = mid_pile
                left_pile = mid_pile + 1
        return amt