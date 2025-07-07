"""
Level: Medium
Link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
Tags: array, greedy, sorting, heap-priority-queue
Description:
You are given an array of events where events[i] = [startDayi, endDayi]. Every
event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You
can only attend one event at any time d.

Return the maximum number of events you can attend.
"""
import heapq
class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        ans = 0
        pq = []
        i = 0
        last_day = max(events, key=lambda x: x[1])[1]
        events.sort()
        for d in range(1, last_day + 1):
            while i < len(events) and events[i][0] <= d:
                heapq.heappush(pq, events[i][1])
                i += 1
            while pq and pq[0] < d:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans += 1
        return ans