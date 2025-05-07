"""
Level: Hard
Link: https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/
Tags: array, two-pointers, binary-search, greedy, queue, sorting, monotonous-queue
Description:
You have n tasks and m workers. Each task has a strength requirement stored in
a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength
to complete. The strength of each worker is stored in a 0-indexed integer array
workers, with the jth worker having workers[j] strength. Each worker can only
be assigned to a single task and must have a strength greater than or equal to
the task's strength requirement (i.e., workers[j] >= tasks[i]).

Additionally, you have pills magical pills that will increase a worker's
strength by strength. You can decide which workers receive the magical pills,
however, you may only give each worker at most one magical pill.

Given the 0-indexed integer arrays tasks and workers and the integers pills and
strength, return the maximum number of tasks that can be completed.
"""
from collections import deque
class Solution:
    def maxTaskAssign(self, tasks: list[int], workers: list[int], pills: int, strength: int) -> int:
        N = len(workers)
        tasks.sort()
        workers.sort()
        left, right = 0, min(N, len(tasks))
        def finishable(midpoint, pillsleft):
            i = 0
            tasks_left = deque()
            for task in range(N - midpoint, N):
                worker = workers[task]
                while i < midpoint and tasks[i] <= worker + strength:
                    tasks_left.append(tasks[i])
                    i += 1
                if not tasks_left:
                    return False
                
                if tasks_left[0] <= worker:
                    tasks_left.popleft()
                else:
                    if pillsleft == 0:
                        return False
                    pillsleft -= 1
                    tasks_left.pop()
            return True
        while left < right:
            middle = (right + left + 1) // 2
            if finishable(middle, pills):
                left = middle
            else:
                right = middle - 1
        return left