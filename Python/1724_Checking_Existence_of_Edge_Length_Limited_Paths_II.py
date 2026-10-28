# Author: Kaustav Ghosh
# Problem: Checking Existence of Edge Length Limited Paths II
# Approach: The queries arrive one at a time rather than as a batch, so they cannot be sorted and answered with a growing union-find as in the simpler version of this problem; instead the structure has to remember its own history. Absorbing the edges in increasing weight and stamping each node with the weight at which it was attached to its parent achieves that: a lookup that climbs only through links stamped below the limit sees exactly the structure as it stood when the limit was reached, so one build serves every query. The merge joins the shallower tree under the deeper one by rank, which keeps the climb logarithmic, and crucially path compression must be left out, since rewriting a parent pointer would discard the history the stamps encode.

class DistanceLimitedPathsExist(object):

    def __init__(self, n, edgeList):
        """
        :type n: int
        :type edgeList: List[List[int]]
        """
        self.parent = list(range(n))
        self.rank = [0] * n
        self.attached_at = [float('inf')] * n
        for u, v, distance in sorted(edgeList, key=lambda edge: edge[2]):
            self._merge(u, v, distance)

    def _root(self, x, limit=float('inf')):
        # Climb only through links created strictly below the limit.
        while self.parent[x] != x and self.attached_at[x] < limit:
            x = self.parent[x]
        return x

    def _merge(self, a, b, distance):
        ra, rb = self._root(a), self._root(b)
        if ra == rb:
            return
        if self.rank[ra] > self.rank[rb]:
            ra, rb = rb, ra
        self.parent[ra] = rb
        self.attached_at[ra] = distance
        if self.rank[ra] == self.rank[rb]:
            self.rank[rb] += 1

    def query(self, p, q, limit):
        """
        :type p: int
        :type q: int
        :type limit: int
        :rtype: bool
        """
        return self._root(p, limit) == self._root(q, limit)


# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)
