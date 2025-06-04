"""
Level: Medium
Link: https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/
Tags: tree, depth-first-search, breadth-first-search
Description:
There exist two undirected trees with n and m nodes, with distinct labels in
ranges [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and
m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge
between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates
that there is an edge between nodes ui and vi in the second tree. You are also
given an integer k.

Node u is target to node v if the number of edges on the path from u to v is
less than or equal to k. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible
number of nodes target to node i of the first tree if you have to connect one
node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you
will remove the added edge before proceeding to the next query.
"""
from collections import defaultdict
class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]], k: int) -> list[int]:
        ans = []
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)
        tree2_max = 0
        def node_search(u_node, parent, adj, k_val):
            if k_val < 0:
                return 0
            current_sum = 1
            if u_node in adj:
                for neighbor in adj[u_node]:
                    if neighbor == parent:
                        continue
                    current_sum += node_search(neighbor, u_node, adj, k_val - 1)
            return current_sum

        if len(edges1) == 0:
            return ans
        if len(edges1) > 0:
            for u, v_node in edges1:
                adj1[u].append(v_node)
                adj1[v_node].append(u)
        if len(edges2) > 0:
            for u, v_node in edges2:
                adj2[u].append(v_node)
                adj2[v_node].append(u)
        if len(edges2) > 0:
            tree2_contribs = []
            for j_node2 in range(len(edges2) + 1):
                tree2_contribs.append(node_search(j_node2, -1, adj2, k - 1))
            if tree2_contribs:
                tree2_max = max(tree2_contribs)
        for i_node1 in range(len(edges1) + 1):
            ans.append(node_search(i_node1, -1, adj1, k) + tree2_max)
        return ans