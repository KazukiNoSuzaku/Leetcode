# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimize-deviation-in-array/

import heapq

class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Normalize: double all odd numbers (maximize them)
        # Then only divide even numbers
        heap = []
        min_val = float('inf')
        for num in nums:
            if num % 2 == 1:
                num *= 2
            heapq.heappush(heap, -num)
            min_val = min(min_val, num)

        result = -heap[0] - min_val
        while heap[0] % 2 == 0:
            top = -heapq.heappop(heap)
            top //= 2
            min_val = min(min_val, top)
            heapq.heappush(heap, -top)
            result = min(result, -heap[0] - min_val)
        return result
