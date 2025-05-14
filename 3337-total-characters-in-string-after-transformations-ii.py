"""
Level: Hard
Link: https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/
Tags: hash-table, math, string, dynamic-programming, counting
Description:
You are given a string s consisting of lowercase English letters, an integer t
representing the number of transformations to perform, and an array nums of
size 26. In one transformation, every character in s is replaced according to
the following rules:
 * Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the
   alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a'
   transforms into the next 3 consecutive characters ahead of it, which results
   in "bcd".
 * The transformation wraps around the alphabet if it exceeds 'z'. For example,
   if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3
   consecutive characters ahead of it, which results in "zab".

Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.
"""
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MOD = 10**9 + 7
        def get_matrix(nums):
            char_matrix = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(1, nums[i] + 1):
                    char_matrix[i][(i + j) % 26] += 1
            return char_matrix

        def matrix_mult(a, b):
            result = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    for k in range(26):
                        result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % MOD
            return result

        def matrix_pow(matrix, power):
            result = [[int(i == j) for j in range(26)] for i in range(26)]
            while power:
                if power % 2:
                    result = matrix_mult(result, matrix)
                matrix = matrix_mult(matrix, matrix)
                power //= 2
            return result
        mat = get_matrix(nums)
        mat_power = matrix_pow(mat, t)
        count = [0] * 26
        for c in s:
            count[ord(c) - 97] += 1
        ans = 0
        for i in range(26):
            for j in range(26):
                ans = (ans + count[i] * mat_power[i][j]) % MOD
        return ans
