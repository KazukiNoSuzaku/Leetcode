# Author: Kaustav Ghosh
# 1061. Lexicographically Smallest Equivalent String
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        parent = list(range(26))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            # Keep the lexicographically smaller as root
            if rx < ry:
                parent[ry] = rx
            else:
                parent[rx] = ry

        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))

        return ''.join(chr(find(ord(c) - ord('a')) + ord('a')) for c in baseStr)
