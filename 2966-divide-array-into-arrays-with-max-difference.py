"""
Level: Medium
Link: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
Tags: array, greedy, sorting
Description:
You are given an integer array nums of size n where n is a multiple of 3 and a
positive integer k.

Divide the array nums into n / 3 arrays of size 3 satisfying the following
condition:
 * The difference between any two elements in one array is less than or equal
   to k.

Return a 2D array containing the arrays. If it is impossible to satisfy the
conditions, return an empty array. And if there are multiple answers, return
any of them.
"""
class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append([nums[i], nums[i + 1], nums[i + 2]])
        return ans
