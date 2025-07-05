"""
Level: Hard
Link: https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/
Tags: math, bit-manipulation, recursion
Description:
Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k. You are also given an integer array
operations, where operations[i] represents the type of the ith operation.

Now Bob will ask Alice to perform all operations in sequence:
 * If operations[i] == 0, append a copy of word to itself.
 * If operations[i] == 1, generate a new string by changing each character in
   word to its next character in the English alphabet, and append it to the
   original word. For example, performing the operation on "c" generates "cd"
   and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word after performing all the
operations.

Note that the character 'z' can be changed to 'a' in the second type of
operation.
"""
class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        ans = 0
        p = 0
        l = 1
        while l < k:
            print(l)
            if operations[p]:
                ans += 1
            l <<= 1
            p += 1
        while p > 0:
            p -= 1
            if k > (l >> 1):
                k -= (l >> 1)
            else:
                if operations[p]:
                    ans -= 1
            l >>= 1
        return chr(97 + (ans % 26))