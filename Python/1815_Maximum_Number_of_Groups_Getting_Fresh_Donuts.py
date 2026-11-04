# Author: Kaustav Ghosh
# Problem: Maximum Number of Groups Getting Fresh Donuts
# Approach: Only each group's size modulo the batch size matters, since whole batches never leave anything behind, so the input collapses to at most nine remainder buckets. Groups whose remainder is zero are always happy, and a group with remainder r followed by one with remainder batchSize minus r leaves the counter back at zero, so those cancelling pairs are taken first and yield one happy group each; after that at most one of every such pair of buckets survives. What remains is settled by a memoised search over the bucket counts, and the counter carried into the next group never needs storing because it is recoverable from which groups are still unserved.

class Solution(object):
    def maxHappyGroups(self, batchSize, groups):
        """
        :type batchSize: int
        :type groups: List[int]
        :rtype: int
        """
        from collections import Counter
        from functools import lru_cache

        remainders = Counter(size % batchSize for size in groups)
        happy = remainders.pop(0, 0)

        for small in range(1, batchSize // 2 + 1):
            large = batchSize - small
            if small == large:
                happy += remainders[small] // 2
                remainders[small] %= 2
            else:
                pairs = min(remainders[small], remainders[large])
                happy += pairs
                remainders[small] -= pairs
                remainders[large] -= pairs

        counts = tuple(remainders[r] for r in range(1, batchSize))
        outstanding = sum((r + 1) * c for r, c in enumerate(counts)) % batchSize

        @lru_cache(maxsize=None)
        def best(left):
            if not any(left):
                return 0
            served = (outstanding - sum((r + 1) * c for r, c in enumerate(left))) % batchSize
            found = 0
            for r, available in enumerate(left):
                if not available:
                    continue
                remaining = left[:r] + (available - 1,) + left[r + 1:]
                score = best(remaining) + (1 if served == 0 else 0)
                if score > found:
                    found = score
            return found

        return happy + best(counts)
