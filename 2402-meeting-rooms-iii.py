"""
Level: Hard
Link: https://leetcode.com/problems/meeting-rooms-iii/
Tags: array, hash-table, sorting, heap-priority-queue, simulation
Description:
You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi]
means that a meeting will be held during the half-closed time interval
[starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:
 * Each meeting will take place in the unused room with the lowest number.
 * If there are no available rooms, the meeting will be delayed until a room
   becomes free. The delayed meeting should have the same duration as the
   original meeting.
 * When a room becomes unused, meetings that have an earlier original start
   time should be given the room.

Return the number of the room that held the most meetings. If there are
multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and
not including b.
"""
import heapq
class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        rooms = list(range(n))
        heapq.heapify(rooms)
        busy_rooms = []
        bookings = [0] * n
        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                b, room = heapq.heappop(busy_rooms)
                heapq.heappush(rooms, room)
            dur = end - start
            if rooms:
                room = heapq.heappop(rooms)
                bookings[room] += 1
                heapq.heappush(busy_rooms, (end, room))
            else:
                first_end, room = heapq.heappop(busy_rooms)
                bookings[room] += 1
                new_end = first_end + dur
                heapq.heappush(busy_rooms, (new_end, room))
        return bookings.index(max(bookings))