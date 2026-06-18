from typing import List
from collections import Counter

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        def is_prime(x):
            if x < 2: return False
            if x < 4: return True
            if x % 2 == 0 or x % 3 == 0: return False
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6
            return True

        cnt = Counter()
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for r in range(m):
            for c in range(n):
                for dr, dc in dirs:
                    num = mat[r][c]
                    nr, nc = r + dr, c + dc
                    while 0 <= nr < m and 0 <= nc < n:
                        num = num * 10 + mat[nr][nc]
                        if is_prime(num):
                            cnt[num] += 1
                        nr += dr
                        nc += dc

        if not cnt:
            return -1
        max_freq = max(cnt.values())
        return max(k for k, v in cnt.items() if v == max_freq)
