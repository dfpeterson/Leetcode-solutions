"""
Level: Easy
Link: https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
Tags: array
Description:
Given an integer array arr, return true if there are three consecutive odd
numbers in the array. Otherwise, return false. 
"""
class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        odds_in_a_row = 0
        for num in arr:
            if num % 2:
                odds_in_a_row += 1
            else:
                odds_in_a_row = 0
            if odds_in_a_row == 3:
                return True
        return False