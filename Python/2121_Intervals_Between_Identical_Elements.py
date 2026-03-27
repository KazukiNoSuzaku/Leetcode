# Author: Kaustav Ghosh
# https://leetcode.com/problems/intervals-between-identical-elements/

from collections import defaultdict

class Solution(object):
    def getDistances(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        groups = defaultdict(list)
        for i, val in enumerate(arr):
            groups[val].append(i)

        result = [0] * len(arr)

        for val, indices in groups.items():
            n = len(indices)
            # Prefix sum of indices
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i + 1] = prefix[i] + indices[i]

            for i in range(n):
                left_sum = indices[i] * i - prefix[i]
                right_sum = (prefix[n] - prefix[i + 1]) - indices[i] * (n - i - 1)
                result[indices[i]] = left_sum + right_sum

        return result
