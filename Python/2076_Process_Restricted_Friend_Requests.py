# Author: Kaustav Ghosh
# Problem 2076: Process Restricted Friend Requests

class Solution(object):
    def friendRequests(self, n, restrictions, requests):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type requests: List[List[int]]
        :rtype: List[bool]
        """
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        result = []
        for u, v in requests:
            pu, pv = find(u), find(v)
            if pu == pv:
                result.append(True)
                continue
            ok = True
            for a, b in restrictions:
                pa, pb = find(a), find(b)
                if (pa == pu and pb == pv) or (pa == pv and pb == pu):
                    ok = False
                    break
            if ok:
                union(u, v)
            result.append(ok)
        return result
