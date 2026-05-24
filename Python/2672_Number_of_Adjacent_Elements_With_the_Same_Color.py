class Solution:
    def colorTheArray(self, n: int, queries: list[list[int]]) -> list[int]:
        colors = [0] * n
        adj = 0
        result = []

        for i, c in queries:
            if colors[i] != 0:
                if i > 0 and colors[i - 1] == colors[i]:
                    adj -= 1
                if i < n - 1 and colors[i + 1] == colors[i]:
                    adj -= 1

            colors[i] = c

            if i > 0 and colors[i - 1] == colors[i]:
                adj += 1
            if i < n - 1 and colors[i + 1] == colors[i]:
                adj += 1

            result.append(adj)

        return result
