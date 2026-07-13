# Author: Kaustav Ghosh
# Problem: Minimize Hamming Distance After Swap Operations
# Approach: Swaps make each connected component freely permutable, so per component match target values against a multiset of the source values; anything unmatched contributes to the distance

from collections import defaultdict, Counter

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

        for a, b in allowedSwaps:
            parent[find(a)] = find(b)

        pool = defaultdict(Counter)
        for i in range(n):
            pool[find(i)][source[i]] += 1

        distance = 0
        for i in range(n):
            bucket = pool[find(i)]
            if bucket[target[i]] > 0:
                bucket[target[i]] -= 1
            else:
                distance += 1
        return distance
