# Author: Kaustav Ghosh
# Problem: Queries on a Permutation With Key (Premium)
# Approach: Simulate with list, find index and move to front

class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        perm = list(range(1, m + 1))
        result = []
        for q in queries:
            idx = perm.index(q)
            result.append(idx)
            perm.pop(idx)
            perm.insert(0, q)
        return result
