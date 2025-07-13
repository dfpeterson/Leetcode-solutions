"""
Level: Hard
Link: https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/
Tags: dynamic-programming, memoization
Description:
There is a tournament where n players are participating. The players are
standing in a single row and are numbered from 1 to n based on their initial
standing position (player 1 is the first player in the row, player 2 is the
second player in the row, etc.).

The tournament consists of multiple rounds (starting from round number 1). In
each round, the ith player from the front of the row competes against the ith
player from the end of the row, and the winner advances to the next round. When
the number of players is odd for the current round, the player in the middle
automatically advances to the next round.
 * For example, if the row consists of players 1, 2, 4, 6, 7
   * Player 1 competes against player 7.
   * Player 2 competes against player 6.
   * Player 4 automatically advances to the next round.

After each round is over, the winners are lined back up in the row based on the
original ordering assigned to them initially (ascending order).

The players numbered firstPlayer and secondPlayer are the best in the
tournament. They can win against any other player before they compete against
each other. If any two other players compete against each other, either of them
might win, and thus you may choose the outcome of this round.

Given the integers n, firstPlayer, and secondPlayer, return an integer array
containing two values, the earliest possible round number and the latest
possible round number in which these two players will compete against each
other, respectively.
"""
from functools import lru_cache
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        @lru_cache
        def check_rounds(l, r, n2):
            if l + r == n2 - 1:
                return [1, 1]
            ans = [float('inf'), float('-inf')]
            m = n2 >> 1
            for i in range(1 << m):
                wins = [False] * n2
                for j in range(m):
                    if i >> j & 1:
                        wins[j] = True
                    else:
                        wins[n2 - 1 - j] = True
                if n2 & 1:
                    wins[m] = True
                wins[n2 - 1 - l], wins[n2 - 1 - r] = False, False
                wins[l], wins[r] = True, True
                l2, r2, n3 = 0, 0, 0
                for j in range(n2):
                    if j == l:
                        l2 = n3
                    if j == r:
                        r2 = n3
                    if wins[j]:
                        n3 += 1
                x, y = check_rounds(l2, r2, n3)
                ans[0] = min(ans[0], x + 1)
                ans[1] = max(ans[1], y + 1)
            return ans
        return check_rounds(firstPlayer - 1, secondPlayer - 1, n)