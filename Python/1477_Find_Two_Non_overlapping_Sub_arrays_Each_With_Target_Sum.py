# Author: Kaustav Ghosh
# Problem: Find Two Non-overlapping Sub-arrays Each With Target Sum
# Approach: Prefix sum with hashmap, track best subarray length ending at or before each index

class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        INF = float('inf')
        best = [INF] * n  # best[i] = min length subarray with sum=target ending at or before i
        prefix = {0: -1}
        s = 0
        result = INF
        for i in range(n):
            s += arr[i]
            if s - target in prefix:
                start = prefix[s - target] + 1
                length = i - start + 1
                if start > 0 and best[start - 1] < INF:
                    result = min(result, length + best[start - 1])
                best[i] = min(best[i - 1] if i > 0 else INF, length)
            else:
                best[i] = best[i - 1] if i > 0 else INF
            prefix[s] = i
        return result if result < INF else -1
