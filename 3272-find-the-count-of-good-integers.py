"""
Level: Hard
Link: https://leetcode.com/problems/find-the-count-of-good-integers/
Tags: hash-table, math, combinatorics, enumeration
Description:
You are given two positive integers n and k.

An integer x is called k-palindromic if:
 * x is a palindrome.
 * x is divisible by k.

An integer is called good if its digits can be rearranged to form a
k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form
the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a
k-palindromic integer.

Return the count of good integers containing n digits.

Note that any integer must not have leading zeros, neither before nor after
rearrangement. For example, 1010 cannot be rearranged to form 101.
"""
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        halfnum = max(n//2,1)
        midnums = [k * (10 ** (n - halfnum - 1)) for k in range(0,10)] if n % 2 and n > 1 else []
        palnums = set()
        perms = 0
        def get_permutes(ordnums):
            last = ''
            cur = 0
            facts = []
            fact = 1
            zerofact = 0
            for z in ordnums:
                if last and z != last:
                    facts.append(cur)
                    cur = 1
                else:
                    cur += 1
                last = z
            facts.append(cur)
            if ordnums[0] == '0':
                zerofact = factorial(len(ordnums) - 1)
                zerofact //= factorial(facts[0] - 1)
                for b in facts[1:]:
                    zerofact //= factorial(b)
            fact = factorial(len(ordnums))
            for b in facts:
                fact //= factorial(b)
            return fact - zerofact

        for num in range(10**(halfnum-1), 10**(halfnum)):
            base = num * (10 ** (n - halfnum))
            if n > 1:
                base += int(''.join([d for d in f'{base}'[::-1]]))
            if midnums:
                for midnum in midnums:
                    if (midnum + base) % k == 0:
                        sortnum = ''.join(sorted(f'{midnum + base}'))
                        if sortnum not in palnums:
                            perms += get_permutes(sortnum)
                            palnums.add(sortnum)
            else:
                if base % k == 0:
                    sortnum = ''.join(sorted(f'{base}'))
                    if sortnum not in palnums:
                        perms += get_permutes(sortnum)
                        palnums.add(sortnum)
        return perms
