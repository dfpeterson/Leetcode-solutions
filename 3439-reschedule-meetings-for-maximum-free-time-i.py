"""
Level: Medium
Link: https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/
Tags: array, greedy, sliding-window
Description:
You are given an integer eventTime denoting the duration of an event, where the
event occurs from time t = 0 to time t = eventTime.

You are also given two integer arrays startTime and endTime, each of length n.
These represent the start and end time of n non-overlapping meetings, where the
ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most k meetings by moving their start time while
maintaining the same duration, to maximize the longest continuous period of
free time during the event.

The relative order of all the meetings should stay the same and they should
remain non-overlapping.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event.
"""
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        ans = 0
        window = 0
        startTime.append(eventTime)
        endTime = [0] + endTime
        for i in range(len(startTime)):
            if i > k:
                window -= startTime[i - k - 1] - endTime[i - k - 1]
            window += startTime[i] - endTime[i]
            if window > ans:
                ans = window
        return ans
