"""
Level: Medium
Link: https://leetcode.com/problems/minimum-time-to-repair-cars/
Tags: array, binary-search
Description:
You are given an integer array ranks representing the ranks of some mechanics.
ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n
cars in r * n2 minutes.

You are also given an integer cars representing the total number of cars
waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.
"""
class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        mintime, maxtime = 1, ranks[0] * (cars**2)
        repaired = -1

        def repair(time):
            totaltime = 0
            for rank in ranks:
                totaltime += int((time / rank) ** 0.5)
            return totaltime

        while mintime <= maxtime:
            trytime = (mintime + maxtime) // 2
            work = repair(trytime)
            if work >= cars:
                repaired = trytime
                maxtime = trytime - 1
            else:
                mintime = trytime + 1

        return repaired