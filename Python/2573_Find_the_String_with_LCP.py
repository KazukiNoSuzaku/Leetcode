class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        # Union-Find: positions sharing lcp>0 must have the same character; assign greedily.
        n = len(lcp)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    pi, pj = find(i), find(j)
                    if pi != pj:
                        parent[pi] = pj

        char_map, s, c = {}, [''] * n, 0
        for i in range(n):
            r = find(i)
            if r not in char_map:
                if c >= 26:
                    return ""
                char_map[r] = chr(ord('a') + c)
                c += 1
            s[i] = char_map[r]
        s = ''.join(s)

        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
            for j in range(i + 1, n):
                exp = (lcp[i + 1][j + 1] + 1 if i + 1 < n and j + 1 < n else 1) if s[i] == s[j] else 0
                if lcp[i][j] != exp or lcp[j][i] != exp:
                    return ""
        return s
