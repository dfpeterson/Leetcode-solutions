"""
Level: Medium
Link: https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/
Tags: two-pointers, string, enumeration
Description:
You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends. There are multiple
rounds in the game, where in each round:
 * word is split into numFriends non-empty strings, such that no previous round
   has had the exact same split.
 * All the split words are put into a box.

Find the lexicographically largest string from the box after all the rounds are
finished.
"""
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        max_char = max(word)
        word_max = len(word) - numFriends + 1
        big_words = set()
        for i in range(len(word)):
            if word[i] == max_char:
                big_words.add(word[i:(i + word_max)])
        return max(big_words)
