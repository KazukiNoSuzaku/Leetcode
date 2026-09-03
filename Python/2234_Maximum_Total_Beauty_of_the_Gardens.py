# Author: Kaustav Ghosh
# Problem: Maximum Total Beauty of the Gardens
# Approach: Clip flowers to target and sort. To be complete it is always cheapest to finish the largest gardens, so iterate over how many gardens stay incomplete (a prefix). For each split, spend the budget to complete the suffix, then use the leftover to raise the minimum of the incomplete prefix as high as possible (capped at target-1) via binary search. Track the best full*complete + partial*min_incomplete

import bisect


class Solution(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        """
        :type flowers: List[int]
        :type newFlowers: int
        :type target: int
        :type full: int
        :type partial: int
        :rtype: int
        """
        a = sorted(min(f, target) for f in flowers)
        n = len(a)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + a[i]

        best = 0
        for i in range(n, -1, -1):
            # complete gardens a[i..n-1]
            cost_complete = (n - i) * target - (pre[n] - pre[i])
            if cost_complete > newFlowers:
                continue
            remain = newFlowers - cost_complete
            complete_cnt = n - i
            if i == 0:
                best = max(best, complete_cnt * full)
                continue
            # raise minimum of a[0..i-1], capped at target-1
            lo, hi = a[0], target - 1
            if lo > hi:
                # every prefix garden already at target (all complete)
                best = max(best, complete_cnt * full)
                continue

            def cost_for(x):
                p = bisect.bisect_left(a, x, 0, i)  # prefix elements strictly below x
                return x * p - pre[p]

            while lo < hi:
                mid = (lo + hi + 1) // 2
                if cost_for(mid) <= remain:
                    lo = mid
                else:
                    hi = mid - 1
            best = max(best, complete_cnt * full + lo * partial)
        return best
