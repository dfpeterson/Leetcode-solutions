"""
Level: Hard
Link: https://leetcode.com/problems/apply-operations-to-maximize-score/
Tags: array, math, stack, greedy, sorting, monotonic-stack, number-theory
Description:
You are given an array nums of n positive integers and an integer k.

Initially, you start with a score of 1. You have to maximize your score by
applying the following operation at most k times:
 * Choose any non-empty subarray nums[l, ..., r] that you haven't chosen
   previously.
 * Choose an element x of nums[l, ..., r] with the highest prime score. If
   multiple such elements exist, choose the one with the smallest index.
 * Multiply your score by x.

Here, nums[l, ..., r] denotes the subarray of nums starting at index l and
ending at the index r, both ends being inclusive.

The prime score of an integer x is equal to the number of distinct prime
factors of x. For example, the prime score of 300 is 3 since
300 = 2 * 2 * 3 * 5 * 5.

Return the maximum possible score after applying at most k operations.

Since the answer may be large, return it modulo 10**9 + 7.
"""
from heapq import heapify, heappop
class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        N = len(nums)
        MOD = 10**9 + 7
        result = 1
        left = [-1] * N 
        right = [N] * N
        stack = []
        primetime = []
        for num in nums:
            score = 0
            for f in range(2, int(num**0.5)+2):
                if num % f == 0:
                    score += 1
                    while num % f == 0:
                        num //= f
            score += (num >= 2)
            primetime.append(score)
        for i, s in enumerate(primetime):
            while stack and primetime[stack[-1]] < s:
                index = stack.pop()
                right[index] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        min_heap = [(-n, i) for i, n in enumerate(nums)]
        heapify(min_heap)
        while k > 0:
            n, index = heappop(min_heap)
            n *= -1
            score = primetime[index]
            left_c = index - left[index]
            right_c = right[index] - index
            count = left_c * right_c
            operations = min(count, k)
            result = (result * pow(n, operations, MOD)) % MOD
            k -= operations
        return result
