"""
Level: hard
Link: https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/
Tags: array, dynamic-programming, heap-priority-queue
Description:
You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from
nums. The remaining 2 * n elements will be divided into two equal parts:
 * The first n elements belonging to the first part and their sum is sumfirst.
 * The next n elements belonging to the second part and their sum is sumsecond.

The difference in sums of the two parts is denoted as sumfirst - sumsecond.
 * For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
 * Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.

Return the minimum difference possible between the sums of the two parts after
the removal of n elements.
"""
from heapq import heapify, heappush, heappop
class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums)//3
        total = sum(nums[:n])
        p_heap = [-x for x in nums[:n]]
        heapify(p_heap)
        precomp = [0] * (2 * n)
        precomp[n - 1] = total
        for i in range(n, 2 * n):
            total += nums[i]
            heappush(p_heap, -nums[i])
            total -= -heappop(p_heap)
            precomp[i] = total

        total = sum(nums[2*n:])
        s_heap = nums[2*n:]
        heapify(s_heap)
        suffix = [0] * (2 * n + 1)
        suffix[2 * n] = total

        for i in range(2 * n - 1, n - 1, -1):
            total += nums[i]
            heappush(s_heap, nums[i])
            total -= heappop(s_heap)
            suffix[i] = total
        ans = float('inf')
        for i in range(n - 1, 2 * n):
            ans = min(ans, precomp[i] - suffix[i + 1])

        return ans