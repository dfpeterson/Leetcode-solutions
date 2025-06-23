"""
Level: Medium
Link: https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/
Tags: hash-table, string, greedy, sorting, counting
Description:
You are given a string word and an integer k.

We consider word to be k-special if |freq(word[i]) - freq(word[j])| <= k for
all indices i and j in the string.

Here, freq(x) denotes the frequency of the character x in word, and |y| denotes
the absolute value of y.

Return the minimum number of characters you need to delete to make word
k-special.
"""
from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        letters = Counter(word).most_common()
        ans = len(word)
        for letter in letters:
            removed = 0
            for comp_letter in letters:
                if comp_letter[1] < letter[1]:
                    removed += comp_letter[1]
                elif comp_letter[1] > letter[1] + k:
                    removed += comp_letter[1] - (letter[1] + k)
            ans = min(ans, removed)
        return ans