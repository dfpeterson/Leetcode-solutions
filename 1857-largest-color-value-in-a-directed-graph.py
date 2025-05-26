"""
Level: Hard
Link: https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
Tags: hash-table, dynamic-programming, graph, topological-sort, memoization, counting
Description:
There is a directed graph of n colored nodes and m edges. The nodes are
numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter
representing the color of the ith node in this graph (0-indexed). You are also
given a 2D array edges where edges[j] = [aj, bj] indicates that there is a
directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk
such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The
color value of the path is the number of nodes that are colored the most
frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if
the graph contains a cycle.
"""
from collections import defaultdict
class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        N = len(colors)
        adj = defaultdict(list)
        ans = 0
        visited, path = set(), set()
        count = [[0] * 26 for i in range(N)]
        for src, dst in edges:
            adj[src].append(dst)

        def node_check(node):
            if node in path:
                return float('inf')
            if node in visited:
                return 0
            visited.add(node)
            path.add(node)
            count[node][ord(colors[node]) - 97] = 1
            for neighbor in adj[node]:
                if node_check(neighbor) == float('inf'):
                    return float('inf')
                for color in range(26):
                    count[node][color] = max(count[node][color], count[neighbor][color] + (color == ord(colors[node]) - 97))
            path.remove(node)
            return max(count[node])

        for i in range(N):
            ans = max(node_check(i), ans)

        return -1 if ans == float('inf') else ans