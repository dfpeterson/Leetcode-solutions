"""
Level: Medium
Link: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
Tags: dynamic-programming, graph, topological-sort, shortest-path
Description:
You are in a city that consists of n intersections numbered from 0 to n - 1
with bi-directional roads between some intersections. The inputs are generated
such that you can reach any intersection from any other intersection and that
there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where
roads[i] = [ui, vi, timei] means that there is a road between intersections ui
and vi that takes timei minutes to travel. You want to know in how many ways
you can travel from intersection 0 to intersection n - 1 in the shortest amount
of time.

Return the number of ways you can arrive at your destination in the shortest
amount of time. Since the answer may be large, return it modulo 10^9 + 7.
"""
class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        nodes = defaultdict(list)
        MOD = 10**9 + 7
        minroute = [(0, 0)]
        values = [float('inf')] * n
        solutions = [1] + ([0] * (n-1))
        for h, t, v in roads:
            nodes[h].append((v, t))
            nodes[t].append((v, h))

        while minroute:
            time, node = heappop(minroute)
            for neighbor_cost, neighbor in nodes[node]:
                if time + neighbor_cost < values[neighbor]:
                    values[neighbor] = time + neighbor_cost
                    solutions[neighbor] = solutions[node]
                    heappush(minroute, (time + neighbor_cost, neighbor))
                elif time + neighbor_cost == values[neighbor]:
                    solutions[neighbor] = (solutions[neighbor] + solutions[node]) % MOD
        return solutions[n-1]
