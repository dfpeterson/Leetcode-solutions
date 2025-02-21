"""
Level: Medium
Link: https://leetcode.com/problems/find-unique-binary-string/
Tags: array, hash-table, string, backtracking
Description:
Given an array of strings nums containing n unique binary strings each of
length n, return a binary string of length n that does not appear in nums. If
there are multiple answers, you may return any of them.
"""
# Original, quick soltuion
class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        numset = set(range(int('1'*len(nums[0]), base=2)+1)) - set([int(num,base=2) for num in nums])
        return f'{min(numset):0{len(nums[0])}b}'

# Second, more efficient solution
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numset = set(nums)
        for k in range(len(nums[0])+1):
            if f'{k:0{len(nums[0])}b}' not in numset:
                return f'{k:0{len(nums[0])}b}'