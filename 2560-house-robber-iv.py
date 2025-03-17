"""
Level: Medium
Link: https://leetcode.com/problems/house-robber-iv/
Tags: array, binary-search
Description:
There are several consecutive houses along a street, each of which has some
money inside. There is also a robber, who wants to steal money from the homes,
but he refuses to steal from adjacent homes.

The capability of the robber is the maximum amount of money he steals from one
house of all the houses he robbed.

You are given an integer array nums representing how much money is stashed in
each house. More formally, the ith house from the left has nums[i] dollars.

You are also given an integer k, representing the minimum number of houses the
robber will steal from. It is always possible to steal at least k houses.

Return the minimum capability of the robber out of all the possible ways to
steal at least k houses.
"""
class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        def valid_robbery(houses):
            vh, vc = 0, 0
            while vh < len(nums):
                if nums[vh] <= houses:
                    vh += 2
                    vc += 1
                else:
                    vh += 1
                if vc == k:
                    break
            return vc == k

        r1, r2 = min(nums), max(nums)
        maxmin = 0
        while r1 <= r2:
            mp = (r2 + r1) // 2
            if valid_robbery(mp):
                maxmin = mp
                r2 = mp - 1
            else:
                r1 = mp + 1
        return maxmin
