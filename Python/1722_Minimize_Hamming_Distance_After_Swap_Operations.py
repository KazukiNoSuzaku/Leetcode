# Author: Kaustav Ghosh
# Problem: Minimize Hamming Distance After Swap Operations
# Approach: A swap can be applied any number of times and in any order, so the positions it links form groups within which the values can be permuted completely freely; union-find builds exactly those groups. Inside a group all that matters is which values are present, not where, so the best possible number of matching positions is the overlap between the group's multiset of source values and its multiset of target values, and everything not covered by that overlap must mismatch. Summing the shortfall over the groups gives the answer without ever constructing an arrangement.

from collections import Counter, defaultdict


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
            root = x
            while parent[root] != root:
                root = parent[root]
            while parent[x] != root:
                parent[x], x = root, parent[x]
            return root

        for a, b in allowedSwaps:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        distance = 0
        for members in groups.values():
            have = Counter(source[i] for i in members)
            want = Counter(target[i] for i in members)
            matched = sum((have & want).values())
            distance += len(members) - matched
        return distance
