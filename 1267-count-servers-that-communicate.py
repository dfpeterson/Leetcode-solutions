"""
Level: Medium
Link: https://leetcode.com/problems/count-servers-that-communicate/
Tags: array, depth-first-search, breadth-first-search, union-find, matrix,
counting
Description:
You are given a map of a server center, represented as a m * n integer matrix
grid, where 1 means that on that cell there is a server and 0 means that it is
no server. Two servers are said to communicate if they are on the same row or
on the same column.

Return the number of servers that communicate with any other server.
"""
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        servers = 0
        grids = len(grid)
        for g in grid:
            gridsum = sum(g)
            checkloc = 0
            if gridsum > 1:
                servers += gridsum
            elif gridsum == 1:
                checkloc = g.index(1)
                remains = 0
                for b in range(grids):
                    if grid[b][checkloc] == 1:
                        remains += 1
                    if remains >= 2:
                        servers += 1
                        break
        return servers
