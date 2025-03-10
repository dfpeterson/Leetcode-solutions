"""
Level: Medium
Link: https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/
Tags: hash-table, string, sliding-window
Description:
You are given a string word and a non-negative integer k.

Return the total number of
of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once
and exactly k consonants.
"""
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def overkcount(j):
            vowels = {l : 0 for l in 'aeiou'}
            consonants = 0
            valid = 0
            p1 = 0
            for p2 in range(len(word)):
                if word[p2] not in 'aeiou':
                    consonants += 1
                else:
                    vowels[word[p2]] += 1
                while all(vowels.values()) and consonants >= j:
                    valid += (len(word) - p2)
                    if word[p1] not in 'aeiou':
                        consonants -= 1
                    else:
                        vowels[word[p1]] -= 1
                    p1 += 1
            return valid
        return overkcount(k) - overkcount(k + 1)