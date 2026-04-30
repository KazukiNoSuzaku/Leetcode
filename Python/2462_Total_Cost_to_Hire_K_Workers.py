import heapq

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        l, r = candidates, n - candidates - 1
        left_heap = costs[:candidates]
        right_heap = costs[n - candidates:] if n - candidates > candidates else []

        # Handle overlap: just pick cheapest k from the full array
        if l > r:
            return sum(sorted(costs)[:k])

        heapq.heapify(left_heap)
        heapq.heapify(right_heap)
        total = 0

        for _ in range(k):
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                total += heapq.heappop(left_heap)
                if l <= r:
                    heapq.heappush(left_heap, costs[l])
                    l += 1
            else:
                total += heapq.heappop(right_heap)
                if l <= r:
                    heapq.heappush(right_heap, costs[r])
                    r -= 1

        return total
