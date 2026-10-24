# Author: Kaustav Ghosh
# Problem: Checking Existence of Edge Length Limited Paths
# Approach: A query asks whether two nodes are joined using only edges below its limit, and the set of usable edges only grows as the limit rises, so the queries are answered out of order: both the edges and the queries are sorted by weight, and a union-find absorbs edges as the limit sweeps upward, each edge being added exactly once overall. At the moment a query is reached, the structure holds precisely the edges it is allowed to use, so the answer is one root comparison. Answers are written back into the original positions so the returned order matches the input.

class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        parent = list(range(n))

        def find(x):
            root = x
            while parent[root] != root:
                root = parent[root]
            while parent[x] != root:
                parent[x], x = root, parent[x]
            return root

        edges = sorted(edgeList, key=lambda edge: edge[2])
        order = sorted(range(len(queries)), key=lambda i: queries[i][2])

        answers = [False] * len(queries)
        position = 0
        for index in order:
            p, q, limit = queries[index]
            while position < len(edges) and edges[position][2] < limit:
                a, b = find(edges[position][0]), find(edges[position][1])
                if a != b:
                    parent[a] = b
                position += 1
            answers[index] = find(p) == find(q)
        return answers
