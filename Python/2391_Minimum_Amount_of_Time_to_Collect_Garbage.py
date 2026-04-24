class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        from itertools import accumulate
        prefix = [0] + list(accumulate(travel))
        total = 0
        for truck in 'MGP':
            last = max((i for i, g in enumerate(garbage) if truck in g), default=0)
            total += prefix[last] + sum(g.count(truck) for g in garbage)
        return total
