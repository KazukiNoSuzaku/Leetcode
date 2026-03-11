# Count groups of strings that are similar (at most 2 swapped positions) transitively.

# Author: Kaustav Ghosh

class Solution(object):
    def numSimilarGroups(self, strs):
        n = len(strs)
        parent = list(range(n))
        def find(x):
            while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def similar(a, b):
            diff = sum(x != y for x, y in zip(a, b))
            return diff == 0 or diff == 2
        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]):
                    pi, pj = find(i), find(j)
                    if pi != pj: parent[pi] = pj
        return sum(find(i) == i for i in range(n))
