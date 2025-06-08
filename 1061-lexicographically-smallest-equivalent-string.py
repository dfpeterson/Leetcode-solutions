"""
Level: Medium
Link: https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
Tags: string, union-find
Description:
You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

 * For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c',
   'b' == 'd', and 'c' == 'e'.

Equivalent characters follow the usual rules of any equivalence relation:
 * Reflexivity: 'a' == 'a'.
 * Symmetry: 'a' == 'b' implies 'b' == 'a'.
 * Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.

For example, given the equivalency information from s1 = "abc" and s2 = "cde",
"acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the
lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the
equivalency information from s1 and s2.
"""
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def get_parent(letter):
            if parent[letter] == letter:
                return letter
            parent[letter] = get_parent(parent[letter])
            return parent[letter]

        def union_find(i, j):
            root_i = get_parent(i)
            root_j = get_parent(j)
            if root_i < root_j:
                parent[root_j] = root_i
            elif root_j < root_i:
                parent[root_i] = root_j

        for a, b in zip(s1, s2):
            union_find(ord(a) - 97, ord(b) - 97)

        return ''.join([chr(parent[get_parent(ord(c) - 97)] + 97) for c in baseStr])