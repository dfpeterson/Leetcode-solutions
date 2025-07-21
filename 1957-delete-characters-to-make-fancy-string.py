"""
Level: Easy
Link: https://leetcode.com/problems/delete-characters-to-make-fancy-string/
Tags: string
Description:
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to
make it fancy.

Return the final string after the deletion. It can be shown that the answer
will always be unique.
"""
class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = [s[0]]
        last = s[0]
        last_count = 1
        for c in s[1:]:
            if c == last:
                if last_count == 2:
                    continue
                last_count += 1
            else:
                last_count = 1
            ans.append(c)
            last = c
        return ''.join(ans)