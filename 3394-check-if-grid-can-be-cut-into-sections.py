"""
Level: Medium
Link: https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/
Tags: array, sorting
Description:
You are given an integer n representing the dimensions of an n x n grid, with
the origin at the bottom-left corner of the grid. You are also given a 2D array
of coordinates rectangles, where rectangles[i] is in the form [startx, starty,
endx, endy], representing a rectangle on the grid. Each rectangle is defined as
follows:
 * (startx, starty): The bottom-left corner of the rectangle.
 * (endx, endy): The top-right corner of the rectangle.

Note that the rectangles do not overlap. Your task is to determine if it is
possible to make either two horizontal or two vertical cuts on the grid such
that:
 * Each of the three resulting sections formed by the cuts contains at least one rectangle.
 * Every rectangle belongs to exactly one section.

Return true if such cuts can be made; otherwise, return false.
"""
class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        def check_cuts(offset):
            slices = 0
            rectangles.sort(key=lambda x: x[offset])
            last_left = rectangles[0][offset]
            last_right = rectangles[0][2 + offset]
            for rectangle in rectangles[1:]:
                if rectangle[offset] >= last_right:
                    slices += 1
                    last_left = rectangle[offset]
                    last_right = rectangle[2 + offset]
                elif rectangle[2 + offset] > last_right:
                    last_right = rectangle[2 + offset]
                if slices >= 2:
                    return True
        for o in [0, 1]:
            if check_cuts(o):
                return True
        return False