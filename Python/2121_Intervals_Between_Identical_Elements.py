# Author: Kaustav Ghosh
# Problem: Intervals Between Identical Elements
# Approach: Group indices by value. Within a group, the sum of absolute distances from one index to all others is computed in O(1) using running left/right sums of positions

from collections import defaultdict

class Solution(object):
    def getDistances(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        groups = defaultdict(list)
        for i, v in enumerate(arr):
            groups[v].append(i)

        answer = [0] * len(arr)
        for idxs in groups.values():
            g = len(idxs)
            total = sum(idxs)
            left_sum = 0
            for k, x in enumerate(idxs):
                right_sum = total - left_sum - x
                answer[x] = (k * x - left_sum) + (right_sum - (g - 1 - k) * x)
                left_sum += x
        return answer
