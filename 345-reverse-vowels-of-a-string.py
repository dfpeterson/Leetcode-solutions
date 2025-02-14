"""
Level: Easy
Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
Tags: two-pointers, string
Description:
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
and upper cases, more than once.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        p1, p2 = 0, len(s)-1
        first_half = []
        second_half = []
        if p1 == p2:
            return s
        while p1 <= p2:
            if word[p1] in 'aeiouAEIOU' and word[p2] in 'aeiouAEIOU':
                first_half.append(word[p2])
                if p1 != p2:
                    second_half.append(word[p1])
                p1 += 1
                p2 -= 1
            else:
                if word[p1] not in 'aeiouAEIOU':
                    first_half.append(word[p1])
                    p1 += 1
                if word[p2] not in 'aeiouAEIOU':
                    if p1 != p2 + 1:
                        second_half.append(word[p2])
                    p2 -= 1
        second_half.reverse()
        return ''.join(first_half + second_half)