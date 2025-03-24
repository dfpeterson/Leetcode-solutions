"""
Level: Medium
Link: https://leetcode.com/problems/count-the-days-without-meetings/
Tags: array, sorting
Description:
You are given a positive integer days representing the total number of days an
employee is available for work (starting from day 1). You are also given a 2D
array meetings of size n where, meetings[i] = [start_i, end_i] represents the
starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no
meetings are scheduled.

Note: The meetings may overlap.
"""
class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        window_start, window_end = meetings[0]
        free_days = window_start - 1
        for meeting in meetings[1:]:
            if meeting[0] > window_end + 1:
                free_days += meeting[0] - window_end - 1
                window_start, window_end = meeting
            elif meeting[1] > window_end:
                window_end = meeting[1]
        free_days += max(0, days - window_end)
        return free_days