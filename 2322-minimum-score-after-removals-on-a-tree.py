"""
Level: Hard
Link: https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/
Tags: array, bit-manipulation, tree, depth-first-search
Description:
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and
n - 1 edges.

You are given a 0-indexed integer array nums of length n where nums[i]
represents the value of the ith node. You are also given a 2D integer array
edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge
between nodes ai and bi in the tree.

Remove two distinct edges of the tree to form three connected components. For a
pair of removed edges, the following steps are defined:
 * Get the XOR of all the values of the nodes for each of the three components
   respectively.
 * The difference between the largest XOR value and the smallest XOR value is
   the score of the pair.
 * For example, say the three components have the node values: [4,5,7], [1,9],
   and [3,3,3]. The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, and
   3 ^ 3 ^ 3 = 3. The largest XOR value is 8 and the smallest XOR value is 3.
   The score is then 8 - 3 = 5.

Return the minimum score of any possible pair of edge removals on the given
tree.
"""
class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        N = len(nums)
        adjacent = [[] for _ in range(N)]
        for u, v in edges:
            adjacent[u].append(v)
            adjacent[v].append(u)
        xor_sum = [0] * N
        in_time = [0] * N
        out_time = [0] * N
        time = 0

        def check_node(u, p):
            nonlocal time
            in_time[u] = time
            time += 1
            xor_sum[u] = nums[u]
            for v in adjacent[u]:
                if v == p:
                    continue
                xor_sum[u] ^= check_node(v, u)
            out_time[u] = time
            return xor_sum[u]

        check_node(0, -1)
        total_xor = xor_sum[0]
        ans = float('inf')

        def is_ancestor(u, v):
            return in_time[u] <= in_time[v] and out_time[v] <= out_time[u]
        
        for i in range(1, N):
            for j in range(i + 1, N):
                part1, part2, part3 = 0, 0, 0
                if is_ancestor(i, j):
                    part1 = xor_sum[j]
                    part2 = xor_sum[i] ^ xor_sum[j]
                    part3 = total_xor ^ xor_sum[i]
                elif is_ancestor(j, i):
                    part1 = xor_sum[i]
                    part2 = xor_sum[j] ^ xor_sum[i]
                    part3 = total_xor ^ xor_sum[j]
                else:
                    part1 = xor_sum[i]
                    part2 = xor_sum[j]
                    part3 = total_xor ^ xor_sum[i] ^ xor_sum[j]
                parts = sorted([part1, part2, part3])
                ans = min(ans, parts[2] - parts[0])
        return ans
