# Author: Kaustav Ghosh
# Problem: Jump Game VI
# Approach: The best score reachable at a position is its own value plus the best score among the k positions behind it, so the recurrence is a maximum over a sliding window rather than over everything seen. A monotonic deque holding candidate indices in decreasing order of their scores answers that in amortised constant time: anything behind a newer, better candidate can never be chosen again and is discarded on arrival, and the front is dropped once it falls out of reach. Each index therefore enters and leaves the deque once, making the whole pass linear instead of multiplying by k.

from collections import deque


class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        best = [0] * n
        best[0] = nums[0]
        window = deque([0])
        for i in range(1, n):
            while window[0] < i - k:
                window.popleft()
            best[i] = best[window[0]] + nums[i]
            while window and best[window[-1]] <= best[i]:
                window.pop()
            window.append(i)
        return best[n - 1]
