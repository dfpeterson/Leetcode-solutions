"""
Level: Medium
Link: https://leetcode.com/problems/count-the-number-of-complete-components/
Tags: depth-first-search, breadth-first-search, union-find, graph
Description:
You are given an integer n. There is an undirected graph with n vertices,
numbered from 0 to n - 1. You are given a 2D integer array edges where
edges[i] = [ai, bi] denotes that there exists an undirected edge connecting
vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path
between any two vertices, and no vertex of the subgraph shares an edge with a
vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between
every pair of its vertices.
"""
class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:

        def node_check(vertex, result):
            if vertex in checked:
                return result
            checked.add(vertex)
            result.append(vertex)
            for neighbor in nody[vertex]:
                node_check(neighbor, result)
            return result

        nody = defaultdict(list)
        valid_nodes = 0
        checked = set()
        for node in edges:
            nody[node[0]].append(node[1])
            nody[node[1]].append(node[0])

        for vert in range(n):
            if vert in checked:
                continue
            obj = node_check(vert, [])
            valid_nodes += all([len(obj) - 1 == len(nody[sub_vert]) for sub_vert in obj])

        return valid_nodes
