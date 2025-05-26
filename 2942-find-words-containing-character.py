"""
Level: Easy
Link: https://leetcode.com/problems/find-words-containing-character/
Tags: array, string
Description:
You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.
"""
class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        return [a for a in [i if x in words[i] else None for i in range(len(words))] if a is not None]