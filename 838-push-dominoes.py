"""
Level: Medium
Link: https://leetcode.com/problems/push-dominoes/
Tags: two-pointers, string, dynamic-programming
Description:
There are n dominoes in a line, and we place each domino vertically upright.
In the beginning, we simultaneously push some of the dominoes either to the
left or to the right.

After each second, each domino that is falling to the left pushes the adjacent
domino on the left. Similarly, the dominoes falling to the right push their
adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays
still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino
expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:
 * dominoes[i] = 'L', if the ith domino has been pushed to the left,
 * dominoes[i] = 'R', if the ith domino has been pushed to the right, and
 * dominoes[i] = '.', if the ith domino has not been pushed.

Return a string representing the final state.
"""
from collections import deque
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        bones = list(dominoes)
        current = deque()
        for idx, domino in enumerate(bones):
            if domino != '.':
                current.append((idx, domino))
        while current:
            idx, domino = current.popleft()
            if domino == 'L' and idx > 0 and bones[idx - 1] == '.':
                current.append((idx - 1, 'L'))
                bones[idx - 1] = 'L'
            elif domino == 'R':
                if idx + 1 < N and bones[idx + 1] == '.':
                    if idx + 2 < N and bones[idx + 2] == 'L':
                        current.popleft()
                    else:
                        current.append((idx + 1, 'R'))
                        bones[idx + 1] = 'R'
        return ''.join(bones)