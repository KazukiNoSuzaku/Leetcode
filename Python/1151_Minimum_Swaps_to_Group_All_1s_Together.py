# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Sliding window of size count(1s), minimize 0s in window

class Solution(object):
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        total_ones = sum(data)
        if total_ones == 0:
            return 0
        window_ones = sum(data[:total_ones])
        max_ones = window_ones
        for i in range(total_ones, len(data)):
            window_ones += data[i] - data[i - total_ones]
            max_ones = max(max_ones, window_ones)
        return total_ones - max_ones
