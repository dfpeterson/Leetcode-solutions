"""
Level: Medium
Link: https://leetcode.com/problems/alternating-groups-ii/
Tags: array, sliding-window
Description:
There is a circle of red and blue tiles. You are given an array of integers
colors and an integer k. The color of tile i is represented by colors[i]:
 * colors[i] == 0 means that tile i is red.
 * colors[i] == 1 means that tile i is blue.

An alternating group is every k contiguous tiles in the circle with alternating
colors (each tile in the group except the first and last one has a different
color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are
considered to be next to each other.
"""
class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        alternates = 1
        res = 0
        for x in range(-k + 1, len(colors) - 1):
            if colors[x] == colors[(x+1)]:
                alternates = 1
            else:
                alternates += 1
            res += k <= alternates
        return res