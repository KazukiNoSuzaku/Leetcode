from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        totals = defaultdict(int)
        for v, w in items1 + items2:
            totals[v] += w
        return sorted(totals.items())
