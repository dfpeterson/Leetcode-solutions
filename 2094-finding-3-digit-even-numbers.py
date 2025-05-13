"""
Level: Easy
Link: https://leetcode.com/problems/finding-3-digit-even-numbers/
Tags: array, hash-table, sorting, enumeration
Description:
You are given an integer array digits, where each element is a digit. The array
may contain duplicates.

You need to find all the unique integers that follow the given requirements:

 * The integer consists of the concatenation of three elements from digits in
   any arbitrary order.
 * The integer does not have leading zeros.
 * The integer is even.

For example, if the given digits were [1, 2, 3], integers 132 and 312 follow
the requirements.

Return a sorted array of the unique integers.
"""
class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        ans = set()
        digits
        for d1 in range(len(digits)):
            if digits[d1] % 2 == 0:
                for d2 in range(len(digits)):
                    if d1 != d2:
                        for d3 in range(len(digits)):
                            if digits[d3] != 0 and d3 != d1 and d3 != d2:
                                ans.add((digits[d3] * 100) + (digits[d2] * 10) + digits[d1])
        return list(sorted(ans))