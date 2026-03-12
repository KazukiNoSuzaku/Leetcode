# Author: Kaustav Ghosh
# 1093. Statistics from a Large Sample
# https://leetcode.com/problems/statistics-from-a-large-sample/

class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        minimum = next(i for i in range(256) if count[i] > 0)
        maximum = next(i for i in range(255, -1, -1) if count[i] > 0)
        total = sum(count)
        mean = sum(i * count[i] for i in range(256)) / float(total)
        mode = max(range(256), key=lambda i: count[i])

        # Median
        mid1, mid2 = (total + 1) // 2, (total + 2) // 2
        median = 0.0
        cumsum = 0
        m1, m2 = None, None
        for i in range(256):
            cumsum += count[i]
            if m1 is None and cumsum >= mid1:
                m1 = i
            if m2 is None and cumsum >= mid2:
                m2 = i
                break
        median = (m1 + m2) / 2.0

        return [float(minimum), float(maximum), mean, median, float(mode)]
