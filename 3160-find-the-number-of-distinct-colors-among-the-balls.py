"""
Level: Medium
Link: https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/
Tags: array, hash-table, simulation
Description:
You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit].
Initially, all balls are uncolored. For every query in queries that is of the
form [x, y], you mark ball x with the color y. After each query, you need to
find the number of distinct colors among the balls.

Return an array result of length n, where result[i] denotes the number of
distinct colors after ith query.

Note that when answering a query, lack of a color will not be considered as a
color.
"""
class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        ball_colors = {}
        colors_used = {}
        color_track = 0
        colors = []
        for k in queries:
            # +1 if it goes into a new color, -1 if it empties an existing color, 0 if it transfers
            last_color = ball_colors.get(k[0], 0)
            ball_colors[k[0]] = k[1]
            if k[1] not in colors_used or colors_used.get(k[1], 0) == 0:
                color_track += 1
                colors_used[k[1]] = 1
                if colors_used.get(last_color, 0) > 0:
                    if colors_used.get(last_color, 0) == 1:
                        color_track -= 1
                    colors_used[last_color] -= 1
            else:
                if colors_used.get(last_color, 0) > 0:
                    if colors_used.get(last_color, 0) == 1 and k[1] != last_color:
                        color_track -= 1
                    colors_used[last_color] -= 1
                colors_used[k[1]] += 1
            colors.append(color_track)
        return colors