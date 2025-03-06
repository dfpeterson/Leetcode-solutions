"""
Level: Medium
Link: https://leetcode.com/problems/count-total-number-of-colored-cells-in-a-matrix/
Tags: math
Description:
There exists an infinitely large two-dimensional grid of uncolored unit cells.
You are given a positive integer n, indicating that you must do the following
routine for n minutes:
 * At the first minute, color any arbitrary unit cell blue.
 * Every minute thereafter, color blue every uncolored cell that touches a blue
   cell.

Below is a pictorial representation of the state of the grid after minutes 1,
2, and 3.

Return the number of colored cells at the end of n minutes.
"""
class Solution:
    def coloredCells(self, n: int) -> int:
        colored = 1
        expanse = 0
        for _ in range(n-1):
            expanse += 4
            colored += expanse
        return colored