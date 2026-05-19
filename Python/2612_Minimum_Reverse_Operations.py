from collections import deque
from sortedcontainers import SortedList

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: list[int], k: int) -> list[int]:
        banned_set = set(banned)
        available = [SortedList(), SortedList()]
        for i in range(n):
            if i != p and i not in banned_set:
                available[i % 2].add(i)

        ans = [-1] * n
        ans[p] = 0
        queue = deque([p])

        while queue:
            pos = queue.popleft()
            # from pos, reachable positions lie in [lo, hi] with step 2
            lo = max(k - 1 - pos, pos - k + 1)
            hi = min(pos + k - 1, 2 * n - k - 1 - pos)
            parity = (pos + k + 1) % 2
            sl = available[parity]
            idx = sl.bisect_left(lo)
            to_remove = []
            while idx < len(sl) and sl[idx] <= hi:
                q = sl[idx]
                ans[q] = ans[pos] + 1
                queue.append(q)
                to_remove.append(q)
                idx += 1
            for q in to_remove:
                sl.remove(q)

        return ans
