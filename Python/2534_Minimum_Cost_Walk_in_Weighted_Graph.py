class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
        # Union-Find; min walk cost within a component = AND of all edge weights in it (start with all-1s).
        parent = list(range(n))
        comp_and = [-1] * n  # -1 = all bits set (identity for AND)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v, w in edges:
            ru, rv = find(u), find(v)
            comp_and[ru] &= w
            comp_and[rv] &= w
            if ru != rv:
                parent[ru] = rv
                comp_and[rv] &= comp_and[ru]

        ans = []
        for s, t in query:
            if s == t:
                ans.append(0)
            elif find(s) != find(t):
                ans.append(-1)
            else:
                ans.append(comp_and[find(s)])
        return ans
