"""
Level: Medium
Link: https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/
Tags: array, graph, heap-priority-queue, matrix, shortest-path
Description:
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j]
represents the minimum time in seconds when you can start moving to that room.
You start from the room (0, 0) at time t = 0 and can move to an adjacent room.
Moving between adjacent rooms takes one second for one move and two seconds
for the next, alternating between the two.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or
vertically.
"""
import heapq
class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        if n == m == 1:
            return 0
        min_arrive_time = [[float('inf')] * m for _ in range(n)]
        min_arrive_time[0][0] = 0
        queue = [(0, 0, 0, 0)]
        drow = [-1, 1, 0, 0]
        dcol = [0, 0, -1, 1]
        while queue:
            cur_cell_time, row, col, move = heapq.heappop(queue)
            if cur_cell_time > min_arrive_time[row][col]:
                continue
            if row == n - 1 and col == m - 1:
                return cur_cell_time
            for row_move, col_move in zip(drow, dcol):
                next_row, next_col = row + row_move, col + col_move
                if 0 <= next_row < n and 0 <= next_col < m:
                    next_move_time = max(cur_cell_time, moveTime[next_row][next_col])
                    neighbor_cell_time = next_move_time + [1, 2][move % 2]
                    if neighbor_cell_time < min_arrive_time[next_row][next_col]:
                        min_arrive_time[next_row][next_col] = neighbor_cell_time
                        heapq.heappush(queue, (neighbor_cell_time, next_row, next_col, move + 1))
        return -1