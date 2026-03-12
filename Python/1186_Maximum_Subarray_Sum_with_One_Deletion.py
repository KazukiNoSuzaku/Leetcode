# Author: Kaustav Ghosh
# DP with two states: max subarray ending here with no deletion and with one deletion

class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 1:
            return arr[0]
        # no_del[i] = max subarray sum ending at i with no deletion
        # one_del[i] = max subarray sum ending at i with exactly one deletion
        no_del = arr[0]
        one_del = float('-inf')
        result = arr[0]
        for i in range(1, n):
            one_del = max(one_del + arr[i], no_del)  # delete arr[i] or delete previous
            no_del = max(no_del + arr[i], arr[i])
            result = max(result, no_del, one_del)
        return result
