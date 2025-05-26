"""
Level: Medium
Link: https://leetcode.com/problems/zero-array-transformation-iii/
Tags: array, greedy, sorting, heap-priority-queue, prefix-sum
Description:
You are given an integer array nums of length n and a 2D array queries where
queries[i] = [li, ri].

Each queries[i] represents the following action on nums:
 * Decrement the value at each index in the range [li, ri] in nums by at most
   1.
 * The amount by which the value is decremented can be chosen independently for
   each index.

A Zero Array is an array with all its elements equal to 0.

Return the maximum number of elements that can be removed from queries, such
that nums can still be converted to a zero array using the remaining queries.
If it is not possible to convert nums to a zero array, return -1.
"""
class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        da = [0] * (len(nums) + 1)
        pq = []

        if len(nums) == 0:
            return len(queries)
        queries.sort()
        query_i = 0
        current_ops = 0
        delta_sum = 0
        for i in range(len(nums)):
            current_ops += da[i]
            while query_i < len(queries) and queries[query_i][0] == i:
                l, r = queries[query_i]
                heapq.heappush(pq, -r)
                query_i += 1
            while current_ops < nums[i]:
                if not pq or -pq[0] < i:
                    return -1
                re = -heapq.heappop(pq)
                current_ops += 1
                if re + 1 < len(nums):
                    da[re + 1] -= 1
            if current_ops < nums[i]:
                return -1
        return len(pq)