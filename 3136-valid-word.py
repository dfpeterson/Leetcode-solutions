"""
Level: Easy
Link: https://leetcode.com/problems/valid-word/
Tags: string
Description:
A word is considered valid if:
 * It contains a minimum of 3 characters.
 * It contains only digits (0-9), and English letters (uppercase and
   lowercase).
 * It includes at least one vowel.
 * It includes at least one consonant.

You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:
 * 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
 * A consonant is an English letter that is not a vowel.
"""
import re
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 or any([l in word for l in '@#$']):
            return False
        vowels = re.compile('[aeiou]', flags=re.I)
        letters = re.compile('[a-z]', flags=re.I) 
        return len(vowels.findall(word)) > 0 and len(letters.findall(word)) - len(vowels.findall(word)) > 0