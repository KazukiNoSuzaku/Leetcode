from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str],
                    changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        # Map each unique substring to an integer id
        sub_id: dict[str, int] = {}
        def get_id(s: str) -> int:
            if s not in sub_id:
                sub_id[s] = len(sub_id)
            return sub_id[s]

        for s in original + changed:
            get_id(s)

        k = len(sub_id)
        dist = [[INF] * k for _ in range(k)]
        for i in range(k):
            dist[i][i] = 0
        for a, b, c in zip(original, changed, cost):
            u, v = get_id(a), get_id(b)
            dist[u][v] = min(dist[u][v], c)
        for mid in range(k):
            for i in range(k):
                if dist[i][mid] == INF:
                    continue
                for j in range(k):
                    if dist[i][mid] + dist[mid][j] < dist[i][j]:
                        dist[i][j] = dist[i][mid] + dist[mid][j]

        n = len(source)
        # dp[i] = min cost to convert source[i:] to target[i:]
        dp = [INF] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            if source[i] == target[i]:
                if dp[i + 1] < INF:
                    dp[i] = dp[i + 1]
            # try all substring replacements starting at i
            for length in range(1, n - i + 1):
                src = source[i:i + length]
                tgt = target[i:i + length]
                if src in sub_id and tgt in sub_id and dp[i + length] < INF:
                    c = dist[sub_id[src]][sub_id[tgt]]
                    if c < INF:
                        dp[i] = min(dp[i], c + dp[i + length])
        return dp[0] if dp[0] < INF else -1
