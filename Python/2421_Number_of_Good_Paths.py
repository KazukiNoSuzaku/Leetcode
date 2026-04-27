from collections import defaultdict

class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        n = len(vals)
        parent = list(range(n))
        comp = {i: (vals[i], 1) for i in range(n)}  # root -> (max_val, count)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        ans = n  # every single node is a valid good path
        for u, v in sorted(edges, key=lambda e: max(vals[e[0]], vals[e[1]])):
            ru, rv = find(u), find(v)
            if ru == rv:
                continue
            mu, cu = comp[ru]
            mv, cv = comp[rv]
            parent[rv] = ru
            if mu > mv:
                comp[ru] = (mu, cu)
            elif mv > mu:
                comp[ru] = (mv, cv)
            else:
                ans += cu * cv
                comp[ru] = (mu, cu + cv)
        return ans
