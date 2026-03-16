# Author: Kaustav Ghosh
# Problem: Maximum Points You Can Obtain from Cards
# Approach: Sliding window: minimize middle window of size n-k

class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        window_size = n - k
        total = sum(cardPoints)
        if window_size == 0:
            return total
        window_sum = sum(cardPoints[:window_size])
        min_window = window_sum
        for i in range(window_size, n):
            window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window = min(min_window, window_sum)
        return total - min_window
