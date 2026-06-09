from typing import List

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        res = 0
        for peak in range(n):
            total = maxHeights[peak]
            cur = maxHeights[peak]
            for i in range(peak - 1, -1, -1):
                cur = min(cur, maxHeights[i])
                total += cur
            cur = maxHeights[peak]
            for i in range(peak + 1, n):
                cur = min(cur, maxHeights[i])
                total += cur
            res = max(res, total)
        return res
