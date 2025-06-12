"""
Level: Hard
Link: https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
Tags: trie
Description:
Given two integers n and k, return the kth lexicographically smallest integer
in the range [1, n].
"""
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        c = 1
        i = 1

        def kcount(cur):
            ans = 0
            neighbor = cur + 1
            while cur <= n:
                neighbor = min(neighbor, n + 1)
                ans += neighbor - cur
                cur *= 10
                neighbor *= 10
            return ans

        while i < k:
            steps = kcount(c)
            if i + steps <= k:
                c += 1
                i += steps
            else:
                c *= 10
                i += 1
        return c