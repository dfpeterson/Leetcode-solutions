"""
Level: Easy
Link: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
Tags: string, sliding-window
Description:
You are given a 0-indexed string blocks of length n, where blocks[i] is either
'W' or 'B', representing the color of the ith block. The characters 'W' and 'B'
denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive
black blocks.

In one operation, you can recolor a white block such that it becomes a black
block.

Return the minimum number of operations needed such that there is at least one
occurrence of k consecutive black blocks.
"""
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        max_blocks = 0
        current = 0
        for point in range(len(blocks)):
            current += blocks[point] == 'B'
            if point >= k:
                current -= blocks[point-k] == 'B'
            max_blocks = max(max_blocks, current)
        return k - max_blocks