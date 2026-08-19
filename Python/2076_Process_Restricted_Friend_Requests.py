# Author: Kaustav Ghosh
# Problem: Process Restricted Friend Requests
# Approach: Union-find over friendships. A request to merge two components is allowed only if no restricted pair would end up split across those exact two components. Check every restriction against the two roots before unioning

class Solution(object):
    def friendRequests(self, n, restrictions, requests):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type requests: List[List[int]]
        :rtype: List[bool]
        """
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        result = []
        for u, v in requests:
            ru, rv = find(u), find(v)
            if ru == rv:
                result.append(True)
                continue
            allowed = True
            for a, b in restrictions:
                ra, rb = find(a), find(b)
                if (ra == ru and rb == rv) or (ra == rv and rb == ru):
                    allowed = False
                    break
            result.append(allowed)
            if allowed:
                parent[ru] = rv
        return result
