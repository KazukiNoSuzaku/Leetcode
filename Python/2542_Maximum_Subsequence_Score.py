import heapq

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # Sort by nums2 descending; for each i as the minimum of nums2, keep top-k nums1 in a min-heap.
        pairs = sorted(zip(nums1, nums2), key=lambda p: -p[1])
        heap = []
        total = ans = 0
        for n1, n2 in pairs:
            heapq.heappush(heap, n1)
            total += n1
            if len(heap) > k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                ans = max(ans, total * n2)
        return ans
