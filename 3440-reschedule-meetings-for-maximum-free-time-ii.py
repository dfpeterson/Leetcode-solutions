"""
Level: Medium
Link: https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/
Tags: array, greedy, enumeration
Description:
You are given an integer eventTime denoting the duration of an event. You are
also given two integer arrays startTime and endTime, each of length n.

These represent the start and end times of n non-overlapping meetings that
occur during the event between time t = 0 and time t = eventTime, where the ith
meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most one meeting by moving its start time while
maintaining the same duration, such that the meetings remain non-overlapping,
to maximize the longest continuous period of free time during the event.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event and
they should remain non-overlapping.

Note: In this version, it is valid for the relative ordering of the meetings to
change after rescheduling one meeting.
"""
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        N = len(startTime)
        ws = [False] * N
        t1, t2 = 0, 0
        ans = 0
        for i in range(N):
            if endTime[i] - startTime[i] <= t1:
                ws[i] = True
            t1 = max(t1, startTime[i] - (endTime[i - 1] if i else 0))
            if endTime[N - i - 1] - startTime[N - i - 1] <= t2:
                ws[N - i - 1] = True
            t2 = max(t2, (startTime[N - i] if i else eventTime) - endTime[N - i - 1])
        for i in range(N):
            l = endTime[i - 1] if i else 0
            r = eventTime if i == len(startTime) - 1 else startTime[i + 1]
            if ws[i]:
                ans = max(ans, r - l)
            else:
                ans = max(ans, r - l - (endTime[i] - startTime[i]))
        return ans