# Given a string num and integer k, make at most k adjacent swaps to get
# the smallest possible integer string.

# Author: Kaustav Ghosh

class Solution(object):
    def minInteger(self, num, k):
        if k >= len(num) * (len(num) - 1) // 2:
            return ''.join(sorted(num))
        num = list(num)
        n = len(num)
        res = []
        used = [False] * n
        remaining = k
        for _ in range(n):
            # Find smallest digit reachable within remaining swaps
            best = '9'
            best_idx = -1
            cost = 0
            for j in range(n):
                if used[j]:
                    continue
                if cost > remaining:
                    break
                if num[j] < best:
                    best = num[j]
                    best_idx = j
                    best_cost = cost
                cost += 1
            res.append(best)
            used[best_idx] = True
            remaining -= best_cost
        return ''.join(res)
