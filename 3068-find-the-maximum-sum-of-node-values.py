"""
Level: Hard
Link: https://leetcode.com/problems/find-the-maximum-sum-of-node-values/
Tags: array, dynamic-programming, greedy, bit-manipulation, tree, sorting
Description:
There exists an undirected tree with n nodes numbered 0 to n - 1. You are given
a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi]
indicates that there is an edge between nodes ui and vi in the tree. You are
also given a positive integer k, and a 0-indexed array of non-negative integers
nums of length n, where nums[i] represents the value of the node numbered i.

Alice wants the sum of values of tree nodes to be maximum, for which Alice can
perform the following operation any number of times (including zero) on the
tree:
 * Choose any edge [u, v] connecting the nodes u and v, and update their values
   as follows:
   * nums[u] = nums[u] XOR k
   * nums[v] = nums[v] XOR k

Return the maximum possible sum of the values Alice can achieve by performing
the operation any number of times.
"""
import heapq
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