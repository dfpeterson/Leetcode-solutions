"""
Level: Hard
Link: https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/
Tags: tree, depth-first-search, breadth-first-search
Description:
There exist two undirected trees with n and m nodes, labeled from [0, n - 1]
and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and
m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge
between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates
that there is an edge between nodes ui and vi in the second tree.

Node u is target to node v if the number of edges on the path from u to v is
even. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible
number of nodes that are target to node i of the first tree if you had to
connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you
will remove the added edge before proceeding to the next query.
"""
from collections import defaultdict, deque
class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]]) -> list[int]:
        def color_nodes(num_nodes, edges):
            adj = defaultdict(list)
            node_colors = [-1] * num_nodes
            color_count = [0, 0]
            q = deque()
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

            if num_nodes == 0:
                return node_colors, color_count
            elif num_nodes > 0:
                q.append((0, 0))
                node_colors[0] = 0
                color_count[0] = 1
                visited = {0}
                while q:
                    cur_node, dist = q.popleft()
                    for neighbor in adj[cur_node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            neighbor_color = (dist + 1) % 2
                            node_colors[neighbor] = neighbor_color
                            color_count[neighbor_color] += 1
                            q.append((neighbor, dist + 1))
            return node_colors, color_count

        colors1, counts1 = color_nodes(len(edges1) + 1, edges1)
        _, counts2 = color_nodes(len(edges2) + 1, edges2)
        tree2_contrib = 0
        if len(edges2) > 0:
            tree2_contrib = max(counts2)
        ans = [0] * (len(edges1) + 1)
        for i in range(len(ans)):
            if len(edges1) == 0:
                break
            tree1_contrib = 0
            tree1_color = colors1[i]
            if tree1_color == 0:
                tree1_contrib = counts1[0]
            elif tree1_color == 1:
                tree1_contrib = counts1[1]
            ans[i] = tree1_contrib + tree2_contrib
        return ans