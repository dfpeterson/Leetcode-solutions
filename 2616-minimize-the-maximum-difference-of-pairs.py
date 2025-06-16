"""
Level: Medium
Link: https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
Tags: array, binary-search, greedy
Description:
You are given a 0-indexed integer array nums and an integer p. Find p pairs of
indices of nums such that the maximum difference amongst all the pairs is
minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this
pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum
of an empty set to be zero.
"""
class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums.sort()
        l, r = 0, 10**9
        ans = 10**9
        def valid_check(t):
            i, c = 0, 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i + 1]) <= t:
                    c += 1
                    i += 2
                else:
                    i += 1
                if c == p:
                    return True
            return False
        
        if p == 0:
            return 0


        while l <= r:
            m = l + (r - l) // 2
            if valid_check(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
