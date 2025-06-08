"""
Level: Medium
Link: https://leetcode.com/problems/lexicographical-numbers/
Tags: depth-first-search, trie
Description:
Given an integer n, return all the numbers in the range [1, n] sorted in
lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space
"""
class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        ans = []
        c = 1
        while len(ans) < n:
            ans.append(c)
            if c * 10 <= n:
                c *= 10
            else:
                while c == n or c % 10 == 9:
                    c //= 10
                c += 1
        return ans