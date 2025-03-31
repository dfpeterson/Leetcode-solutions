"""
Level: Hard
Link: https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/
Tags: array, two-pointers, breadth-first-search, union-find, sorting, heap-priority-queue, matrix
Description:
You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start
in the top left cell of the matrix and repeat the following process:
 * If queries[i] is strictly greater than the value of the current cell that
   you are in, then you get one point if it is your first time visiting this
   cell, and you can move to any adjacent cell in all 4 directions: up, down,
   left, and right.
 * Otherwise, you do not get any points, and you end this process.

After the process, answer[i] is the maximum number of points you can get. Note
that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.
"""
from collections import defaultdict
class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        #bfs for dead ends and count
        q2 = queries.copy()
        q2.sort()
        moves = defaultdict(int)
        move_check = [(0, 0)]
        max_x, max_y = len(grid), len(grid[0])
        validated = set()
        current = 0
        for q in q2:
            if q in moves:
                continue
            next_moves = []
            current_check = validated.copy()
            while move_check:
                coordinate = move_check.pop()
                x, y = coordinate
                if coordinate not in current_check:
                    if grid[x][y] < q:
                        current += 1
                        if x > 0 and (x - 1, y) not in current_check:
                            move_check.append((x - 1, y))
                        if x < (max_x - 1) and (x + 1, y) not in current_check:
                            move_check.append((x + 1, y))
                        if y > 0 and (x, y - 1) not in current_check:
                            move_check.append((x, y - 1))
                        if y < (max_y - 1) and (x, y + 1) not in current_check:
                            move_check.append((x, y + 1))
                        validated.add(coordinate)
                    else:
                        next_moves.append(coordinate)
                    current_check.add(coordinate)
            moves[q] = current
            move_check = next_moves
        return [moves[q] for q in queries]
