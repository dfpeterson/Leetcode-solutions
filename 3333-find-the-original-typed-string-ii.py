"""
Level: Hard
Link: https://leetcode.com/problems/find-the-original-typed-string-ii
Tags: 
Description:
Alice is attempting to type a specific string on her computer. However, she
tends to be clumsy and may press a key for too long, resulting in a character
being typed multiple times.

You are given a string word, which represents the final output displayed on
Alice's screen. You are also given a positive integer k.

Return the total number of possible original strings that Alice might have
intended to type, if she was trying to type a string of size at least k.

Since the answer may be very large, return it modulo 109 + 7.
"""
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        n, counter = len(word), 1
        frequencies = []
        for i in range(1, n):
            if word[i] == word[i - 1]:
                counter += 1
            else:
                frequencies.append(counter)
                counter = 1
        frequencies.append(counter)
        ans = 1
        for o in frequencies:
            ans = ans * o % MOD
        if len(frequencies) >= k:
            return ans
        
        f = [1] + [0] * (k - 1)
        g = [1] * k
        for i in range(len(frequencies)):
            f_new = [0] * k
            for j in range(1, k):
                f_new[j] = g[j - 1]
                if j - frequencies[i] - 1 >= 0:
                    f_new[j] = (f_new[j] - g[j - frequencies[i] - 1]) % MOD
            g_new = [f_new[0]] + [0] * (k - 1)
            for j in range(1, k):
                g_new[j] = (g_new[j - 1] + f_new[j]) % MOD
            f, g = f_new, g_new
        return (ans - g[k - 1]) % MOD