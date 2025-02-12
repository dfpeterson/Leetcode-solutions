"""
Level: Medium
Link: https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
Tags: array, hash-table, sorting, heap-priority-queue
Description:
You are given a 0-indexed array nums consisting of positive integers. You can
choose two indices i and j, such that i != j, and the sum of digits of the
number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all
possible indices i and j that satisfy the conditions.
"""
class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        digisum = {}
        biggest = -1
        for number in nums:
            sumofadig = sum([int(k) for k in f'{number}'])
            if sumofadig in digisum:
                biggest = max(number + digisum[sumofadig], biggest)
                digisum[sumofadig] = max(digisum[sumofadig], number)
            else:
                digisum[sumofadig] = number
        return biggest