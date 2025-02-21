"""
Level: Medium
Link: https://leetcode.com/problems/letter-tile-possibilities/
Tags: hash-table, string, backtracking, counting
Description:
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using
the letters printed on those tiles.
"""
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        letters = {}
        for letter in tiles:
            letters[letter] = letters.get(letter, 0) + 1
        def permutes():
            permutations = 0
            for letter in letters:
                if letters[letter]:
                    letters[letter] -= 1
                    permutations += 1 + permutes()
                    letters[letter] += 1
            return permutations
        return permutes()