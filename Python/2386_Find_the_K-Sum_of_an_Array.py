import heapq

class Solution:
    def kSum(self, nums: list[int], k: int) -> int:
        # Max sum = sum of all positives
        # Any other subset sum = max_sum - sum of abs values of some elements
        # (replacing a positive with 0 costs its value; adding a negative costs |neg|)
        max_sum = sum(x for x in nums if x > 0)
        abs_sorted = sorted(abs(x) for x in nums)

        # Min-heap of (cost_reduction, index): find k smallest cost reductions
        heap = [(abs_sorted[0], 0)]
        result = [max_sum]
        while len(result) < k:
            cost, i = heapq.heappop(heap)
            result.append(max_sum - cost)
            if i + 1 < len(abs_sorted):
                heapq.heappush(heap, (cost + abs_sorted[i + 1], i + 1))
                heapq.heappush(heap, (cost - abs_sorted[i] + abs_sorted[i + 1], i + 1))
        return result[k - 1]
