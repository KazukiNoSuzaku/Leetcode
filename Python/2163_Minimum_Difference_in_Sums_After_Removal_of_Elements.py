# Author: Kaustav Ghosh
# Problem: 2163. Minimum Difference in Sums After Removal of Elements
# URL: https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/
# Difficulty: Hard

import heapq

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 3

        # prefix[i] = min sum of n elements from nums[0..i]
        prefix = [0] * (3 * n + 1)
        min_heap = []
        cur_sum = 0
        for i in range(n):
            heapq.heappush(min_heap, -nums[i])
            cur_sum += nums[i]
        prefix[n] = cur_sum
        for i in range(n, 2 * n):
            heapq.heappush(min_heap, -nums[i])
            cur_sum += nums[i]
            cur_sum += heapq.heappop(min_heap)  # heappop gives most negative = largest
            prefix[i + 1] = cur_sum

        # suffix[i] = max sum of n elements from nums[i..3n-1]
        suffix = [0] * (3 * n + 1)
        max_heap = []
        cur_sum = 0
        for i in range(3 * n - 1, 2 * n - 1, -1):
            heapq.heappush(max_heap, nums[i])
            cur_sum += nums[i]
        suffix[2 * n] = cur_sum
        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(max_heap, nums[i])
            cur_sum += nums[i]
            cur_sum -= heapq.heappop(max_heap)
            suffix[i] = cur_sum

        return min(prefix[i] - suffix[i] for i in range(n, 2 * n + 1))
