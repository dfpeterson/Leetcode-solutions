"""
Level: Hard
Link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii
Tags: array, binary-search, dynamic-programming, sorting
Description:
You are given an array of events where events[i] = [startDayi, endDayi, valuei].
The ith event starts at startDayi and ends at endDayi, and if you attend this
event, you will receive a value of valuei. You are also given an integer k
which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you
must attend the entire event. Note that the end day is inclusive: that is, you
cannot attend two events where one of them starts and the other ends on the
same day.

Return the maximum sum of values that you can receive by attending events.
"""
from bisect import bisect_left
from functools import lru_cache
class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort()
        starts = [e[0] for e in events]

        @lru_cache(None)
        def check_events(current, count):
            if count == 0 or current == len(events):
                return 0
            next_i = bisect_left(starts, events[current][1] + 1)
            ans = max(events[current][2] + check_events(next_i, count - 1), check_events(current + 1, count))
            return ans
        return check_events(0, k)