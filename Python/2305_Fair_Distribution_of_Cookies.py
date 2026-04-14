# Author: Kaustav Ghosh
class Solution(object):
    def distributeCookies(self, cookies, k):
        # type: (List[int], int) -> int
        n = len(cookies)
        dist = [0] * k
        self.ans = float('inf')

        def backtrack(i):
            if i == n:
                self.ans = min(self.ans, max(dist))
                return
            for j in range(k):
                if dist[j] + cookies[i] >= self.ans:
                    continue
                dist[j] += cookies[i]
                backtrack(i + 1)
                dist[j] -= cookies[i]
                if dist[j] == 0:
                    break

        backtrack(0)
        return self.ans
