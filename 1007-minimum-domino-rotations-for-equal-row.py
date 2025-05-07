"""
Level: Medium
Link: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
Tags: array, greedy
Description:
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom
halves of the ith domino. (A domino is a tile with two numbers from 1 to 
6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the
same, or all the values in bottoms are the same.

If it cannot be done, return -1.
"""
class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        for target in (tops[0], bottoms[0]):
            top_flip, bottom_flip = 0, 0
            for i in range(len(tops)):
                if bottoms[i] != target and tops[i] != target:
                    break
                if target != bottoms[i]:
                    bottom_flip += 1
                if target != tops[i]:
                    top_flip += 1
                if i == len(tops) - 1:
                    return min(top_flip, bottom_flip)
        return -1