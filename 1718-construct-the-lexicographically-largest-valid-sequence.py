"""
Level: Medium
Link: https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/
Tags: arrays, backtracking
Description:
Given an integer n, find a sequence that satisfies all of the following:
 * The integer 1 occurs once in the sequence.
 * Each integer between 2 and n occurs twice in the sequence.
 * For every integer i between 2 and n, the distance between the two
   occurrences of i is exactly i.

The distance between two numbers on the sequence, a[i] and a[j], is the
absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the
given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length)
if in the first position where a and b differ, sequence a has a number greater
than the corresponding number in b. For example, [0,1,9,0] is lexicographically
larger than [0,1,5,6] because the first position they differ is at the third
number, and 9 is greater than 5.
"""
class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        results = [0] * (2 * n - 1)
        placed = set()
        def backtrack(pos):
            if pos == (2 * n - 1):
                return True        
            for num in range(n, 0, -1):
                if (num in placed) or (num > 1 and (num + pos >= (2 * n - 1) or results[num + pos])):
                    continue
                placed.add(num)
                results[pos] = num
                if num > 1:
                    results[pos+num] = num
                pointer = pos + 1
                while pointer < (2 * n - 1) and results[pointer]:
                    pointer += 1
                if backtrack(pointer):
                    return True
                placed.remove(num)
                results[pos] = 0
                if num > 1:
                    results[pos+num] = 0
            return False
        backtrack(0)
        return results