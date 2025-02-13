"""
Level: Easy
Link: https://leetcode.com/problems/can-place-flowers/
Tags: array, greedy
Description:
You have a long flowerbed in which some of the plots are planted, and some are
not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty
and 1 means not empty, and an integer n, return true if n new flowers can be
planted in the flowerbed without violating the no-adjacent-flowers rule and
false otherwise.
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        plant_slots = 0
        seed_window = 0
        for space in [0] + flowerbed + [0]:
            if space == 1:
                seed_window = 0
            else:
                seed_window += 1
            if seed_window > 1 and seed_window % 2:
                plant_slots += 1
            if plant_slots == n:
                return True
        return False