from collections import Counter

class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        # Excess fruits combined, sorted; swap cheapest half using direct swap or relay via global min.
        cnt = Counter(basket1)
        for x in basket2:
            cnt[x] -= 1
        global_min = min(basket1 + basket2)
        excess = []
        for fruit, diff in cnt.items():
            if diff % 2 != 0:
                return -1
            excess.extend([fruit] * (abs(diff) // 2))
        excess.sort()
        return sum(min(v, 2 * global_min) for v in excess[:len(excess) // 2])
