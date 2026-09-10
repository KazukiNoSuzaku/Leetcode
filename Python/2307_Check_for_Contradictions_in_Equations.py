# Author: Kaustav Ghosh
# Problem: Check for Contradictions in Equations
# Approach: Weighted union-find where each variable stores its ratio to its component root. For each equation a/b = v, if a and b are already connected, verify the implied ratio matches v within a small tolerance (a contradiction otherwise); if not connected, union them and set the weight so the ratio holds

class Solution(object):
    def checkContradictions(self, equations, values):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :rtype: bool
        """
        parent = {}
        weight = {}  # weight[x] = value of x / value of parent[x]

        def find_ratio(x):
            # returns (root, x/root)
            if x not in parent:
                parent[x] = x
                weight[x] = 1.0
                return x, 1.0
            path = []
            while parent[x] != x:
                path.append(x)
                x = parent[x]
            root = x
            ratio = 1.0
            for node in reversed(path):
                ratio = weight[node] * ratio  # node/root = weight[node]*(parent/root)
                parent[node] = root
                weight[node] = ratio
            return root, (weight[path[0]] if path else 1.0)

        EPS = 1e-5
        for (a, b), v in zip(equations, values):
            ra, wa = find_ratio(a)   # wa = a/ra
            rb, wb = find_ratio(b)   # wb = b/rb
            if ra == rb:
                # a/b = wa/wb ; must equal v
                if abs(wa - v * wb) > EPS * max(1.0, abs(v * wb)):
                    return True
            else:
                # attach ra under rb: a/b = v => a = v*b
                # ra: root of a with a = wa*ra ; rb root with b = wb*rb
                # want a/b = v -> wa*ra / (wb*rb) = v -> ra/rb = v*wb/wa
                parent[ra] = rb
                weight[ra] = v * wb / wa
        return False
