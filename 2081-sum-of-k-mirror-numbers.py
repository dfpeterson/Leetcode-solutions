"""
Level: Hard
Link: https://leetcode.com/problems/sum-of-k-mirror-numbers/
Tags: math, enumeration
Description:
A k-mirror number is a positive integer without leading zeros that reads the
same both forward and backward in base-10 as well as in base-k.
 * For example, 9 is a 2-mirror number. The representation of 9 in base-10 and
   base-2 are 9 and 1001 respectively, which read the same both forward and
   backward.
 * On the contrary, 4 is not a 2-mirror number. The representation of 4 in
   base-2 is 100, which does not read the same both forward and backward.

Given the base k and the number n, return the sum of the n smallest k-mirror
numbers.
"""
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def base_conv(num):
            if num == '0':
                return '0'
            num = int(num)
            ans = ''
            while num:
                ans = f'{num % k}{ans}'
                num //= k
            return ans

        ns = 0
        ans = 0
        k_len = 1
        while ns < n:
            for i in range(10**(k_len - 1), 10**(k_len)):
                s = f'{i}'
                numstr = s + s[:-1][::-1]
                k_str = base_conv(numstr)
                if k_str == k_str[::-1]:
                    ns += 1
                    ans += int(numstr)
                    if ns == n:
                        return ans
            for i in range(10**(k_len - 1), 10**(k_len)):
                s = f'{i}'
                numstr = s + s[::-1]
                k_str = base_conv(numstr)
                if k_str == k_str[::-1]:
                    ns += 1
                    ans += int(numstr)
                    if ns == n:
                        return ans
            k_len += 1
        return ans