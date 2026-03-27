# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

import bisect

class Solution(object):
    def kIncreasing(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        def lis_length(seq):
            # Longest non-decreasing subsequence using bisect_right
            tails = []
            for x in seq:
                pos = bisect.bisect_right(tails, x)
                if pos == len(tails):
                    tails.append(x)
                else:
                    tails[pos] = x
            return len(tails)

        result = 0
        for start in range(k):
            subseq = []
            i = start
            while i < len(arr):
                subseq.append(arr[i])
                i += k
            result += len(subseq) - lis_length(subseq)
        return result
