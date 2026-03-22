# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

from collections import Counter

class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        n = len(source)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb

        for a, b in allowedSwaps:
            union(a, b)

        # Group indices by connected component
        groups = {}
        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)

        result = 0
        for indices in groups.values():
            src_count = Counter(source[i] for i in indices)
            tgt_count = Counter(target[i] for i in indices)
            # Count matches
            matches = 0
            for val in src_count:
                if val in tgt_count:
                    matches += min(src_count[val], tgt_count[val])
            result += len(indices) - matches

        return result
