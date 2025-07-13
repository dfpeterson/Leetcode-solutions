"""
Level: Medium
Link: https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
Tags: array, two-pointers, greedy, sorting
Description:
You are given a 0-indexed integer array players, where players[i] represents
the ability of the ith player. You are also given a 0-indexed integer array
trainers, where trainers[j] represents the training capacity of the jth
trainer.

The ith player can match with the jth trainer if the player's ability is less
than or equal to the trainer's training capacity. Additionally, the ith player
can be matched with at most one trainer, and the jth trainer can be matched
with at most one player.

Return the maximum number of matchings between players and trainers that
satisfy these conditions.
"""
class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        ans = 0
        while players and trainers:
            player = players.pop()
            if player <= trainers[-1]:
                ans += 1
                trainers.pop()
        return ans