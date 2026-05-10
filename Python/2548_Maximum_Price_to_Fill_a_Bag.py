class Solution:
    def maxPrice(self, items: list[list[int]], capacity: int) -> float:
        # Fractional knapsack: greedy by price-per-weight ratio descending; return -1 if can't fill exactly.
        items.sort(key=lambda x: x[1] / x[0], reverse=True)
        total = 0.0
        for w, p in items:
            take = min(w, capacity)
            total += take * p / w
            capacity -= take
            if capacity == 0:
                return total
        return -1.0
