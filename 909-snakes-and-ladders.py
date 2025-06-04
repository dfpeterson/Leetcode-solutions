"""
Level: Medium
Link: https://leetcode.com/problems/snakes-and-ladders/
Tags: array, breadth-first-search, matrix
Description:
You are given an n x n integer matrix board where the cells are labeled from 1
to n2 in a Boustrophedon style starting from the bottom left of the board (i.e.
board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do
the following:
 * Choose a destination square next with a label in the range [curr + 1,
   min(curr + 6, n2)].
   * This choice simulates the result of a standard 6-sided die roll: i.e.,
     there are always at most 6 destinations, regardless of the size of the
     board.
 * If next has a snake or ladder, you must move to the destination of that
   snake or ladder. Otherwise, you move to next.
 * The game ends when you reach the square n2.

A board square on row r and column c has a snake or ladder if
board[r][c] != -1. The destination of that snake or ladder is board[r][c].
Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the
destination to a snake or ladder is the start of another snake or ladder, you
do not follow the subsequent snake or ladder.
 * For example, suppose the board is [[-1,4],[-1,3]], and on the first move,
   your destination square is 2. You follow the ladder to square 3, but do not
   follow the subsequent ladder to 4.

Return the least number of dice rolls required to reach the square n2. If it is
not possible to reach the square, return -1.
"""
from collections import deque
class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        board_len = len(board)
        q = deque()
        q.append((1, 0))
        visited = set()
        board.reverse()
        def get_pos(sq):
            r = (sq - 1) // board_len
            c = (sq - 1) % board_len
            if r % 2:
                c = board_len - 1 - c
            return (r, c)
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                next_square = square + i
                r, c = get_pos(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == board_len ** 2:
                    return moves + 1
                if next_square not in visited:
                    visited.add(next_square)
                    q.append((next_square, moves + 1))
        return -1
