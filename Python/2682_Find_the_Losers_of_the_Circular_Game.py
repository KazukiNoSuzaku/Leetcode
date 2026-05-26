class Solution:
    def circularGameLosers(self, n: int, k: int) -> list[int]:
        visited = [False] * n
        cur, turn = 0, 1
        while not visited[cur]:
            visited[cur] = True
            cur = (cur + turn * k) % n
            turn += 1
        return [i + 1 for i in range(n) if not visited[i]]
