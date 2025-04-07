"""
Level: Medium
Link: https://leetcode.com/problems/largest-divisible-subset/
Tags: array, math, dynamic-programming, sorting
Description:
Given a set of distinct positive integers nums, return the largest subset
answer such that every pair (answer[i], answer[j]) of elements in this
subset satisfies:
 * answer[i] % answer[j] == 0, or
 * answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.
"""
class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        gcfs = [0] * len(nums)
        parent = [0] * len(nums)
        max_pos = 0
        max_gcfs = 0
        ans = []
        for num_pos in range(len(nums)):
            for back in range(num_pos, -1, -1):
                if nums[num_pos] % nums[back] == 0:
                    if gcfs[back] >= gcfs[num_pos]:
                        gcfs[num_pos] = 1 + gcfs[back]
                        parent[num_pos] = back
            if gcfs[num_pos] > max_gcfs:
                max_gcfs = gcfs[num_pos]
                max_pos = num_pos
        ans.append(nums[max_pos])
        while parent[max_pos] != max_pos:
            max_pos = parent[max_pos]
            ans.append(nums[max_pos])
        return ans[::-1]
