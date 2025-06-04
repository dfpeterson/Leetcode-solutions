"""
Level: Medium
Link: https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
Tags: depth-first-search, graph
Description:
You are given a directed graph of n nodes numbered from 0 to n - 1, where each
node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n,
indicating that there is a directed edge from node i to node edges[i]. If there
is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2,
such that the maximum between the distance from node1 to that node, and from
node2 to that node is minimized. If there are multiple answers, return the node
with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.
"""
from collections import deque
class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        def get_dist(start_node):
            distances = [-1] * len(edges)
            if start_node == -1:
                return distances
            q = deque()
            distances[start_node] = 0
            q.append((start_node, 0))
            while q:
                cur_node, dist = q.popleft()
                neighbor = edges[cur_node]
                if neighbor != -1 and distances[neighbor] == -1:
                    distances[neighbor] = dist + 1
                    q.append((neighbor, dist + 1))
            return distances

        d1, d2 = get_dist(node1), get_dist(node2)
        min_max_dist = float('inf')
        ans_node = -1
        for i in range(len(edges)):
            if d1[i] != -1 and d2[i] != -1:
                current_dist = max(d1[i], d2[i])
                if current_dist < min_max_dist:
                    min_max_dist = current_dist
                    ans_node = i
                elif current_dist == min_max_dist:
                    if ans_node == -1 or i < ans_node:
                        ans_node
        return ans_node