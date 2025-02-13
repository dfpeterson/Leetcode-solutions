"""
Level: Medium
Link: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/
Tags: array, heap-priority-queue, simulation
Description:
You are given a 0-indexed integer array nums, and an integer k.

In one operation, you will:
 * Take the two smallest integers x and y in nums.
 * Remove x and y from nums.
 * Add min(x, y) * 2 + max(x, y) anywhere in the array.

Note that you can only apply the described operation if nums contains at least
two elements.

Return the minimum number of operations needed so that all elements of the
array are greater than or equal to k.
"""
import heapq
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        ops = 0
        heapq.heapify(nums)
        while nums[0] < k:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, (min(x, y) * 2) + max(x, y))
            ops += 1
        return ops