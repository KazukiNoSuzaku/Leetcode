# Find shortest superstring containing all given words as substrings.

# Author: Kaustav Ghosh

class Solution(object):
    def shortestSuperstring(self, words):
        n = len(words)
        overlap = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    for k in range(min(len(words[i]),len(words[j])), 0, -1):
                        if words[i].endswith(words[j][:k]):
                            overlap[i][j] = k; break
        dp = [[float('inf')]*n for _ in range(1<<n)]
        parent = [[-1]*n for _ in range(1<<n)]
        for i in range(n): dp[1<<i][i] = len(words[i])
        for mask in range(1<<n):
            for last in range(n):
                if not (mask>>last&1) or dp[mask][last]==float('inf'): continue
                for nxt in range(n):
                    if mask>>nxt&1: continue
                    nm = mask|(1<<nxt)
                    new_cost = dp[mask][last] + len(words[nxt]) - overlap[last][nxt]
                    if new_cost < dp[nm][nxt]:
                        dp[nm][nxt] = new_cost
                        parent[nm][nxt] = last
        full = (1<<n)-1
        last = min(range(n), key=lambda x: dp[full][x])
        path = []
        mask = full
        while last != -1:
            path.append(last)
            prev = parent[mask][last]
            mask ^= (1<<last)
            last = prev
        path.reverse()
        res = words[path[0]]
        for i in range(1, n):
            res += words[path[i]][overlap[path[i-1]][path[i]]:]
        return res
