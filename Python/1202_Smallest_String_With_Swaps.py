# Author: Kaustav Ghosh
# Union-Find to group indices, sort characters within each component

class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        from collections import defaultdict
        n = len(s)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        for a, b in pairs:
            union(a, b)

        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        result = list(s)
        for indices in groups.values():
            chars = sorted(result[i] for i in indices)
            for i, idx in enumerate(sorted(indices)):
                result[idx] = chars[i]
        return ''.join(result)
