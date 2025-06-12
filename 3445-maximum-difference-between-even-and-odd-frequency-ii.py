"""
Level: Hard
Link: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency/
Tags: string, sliding-window, enumeration, prefix-sum
Description:
You are given a string s and an integer k. Your task is to find the maximum
difference between the frequency of two characters, freq[a] - freq[b], in a
substring subs of s, such that:
 * subs has a size of at least k.
 * Character a has an odd frequency in subs.
 * Character b has an even frequency in subs.

Return the maximum difference.

Note that subs can contain more than 2 distinct characters.
"""
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        N = len(s)
        ans = float('-inf')
        def check_nums(n1, n2):
            return ((n1 & 1) << 1) | (n2 & 1)

        for a in range(5):
            for b in range(5):
                if a == b:
                    continue
                diffs = [float('inf')] * 4
                count_a, count_b = 0, 0
                prev_a, prev_b = 0, 0
                l = -1
                for r in range(N):
                    count_a += s[r] == str(a)
                    count_b += s[r] == str(b)
                    while r - l >= k and count_b - prev_b >= 2:
                        status = check_nums(prev_a, prev_b)
                        diffs[status] = min(diffs[status], prev_a - prev_b)
                        l += 1
                        prev_a += s[l] == str(a)
                        prev_b += s[l] == str(b)
                    status = check_nums(count_a, count_b)
                    if diffs[status ^ 2] < float('inf'):
                        ans = max(ans, (count_a - count_b) - diffs[status ^ 2])
        return ans