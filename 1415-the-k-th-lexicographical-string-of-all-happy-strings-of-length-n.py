"""
Level: Medium
Link: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
Tags: string, backtracking
Description:
A happy string is a string that:
 * consists only of letters of the set ['a', 'b', 'c'].
 * s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is
   1-indexed).

For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings
and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n
sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less
than k happy strings of length n.
"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        choices = ['a', 'b', 'c']
        combos = 3 * max((2 ** (n-1)), 1)
        pointer = k
        results = []
        if k > combos:
            return ''
        layer = ''.join([letter * int(combos/3) for letter in choices])
        results.append(layer[pointer-1])
        combos /= 3
        pointer = (pointer % int(combos))
        while combos > 1:
            layer = ''.join([letter * int(combos/2) for letter in choices if letter != results[-1]])
            results.append(layer[pointer-1])
            combos /= 2
            pointer = (pointer % int(combos))
        return ''.join(results)