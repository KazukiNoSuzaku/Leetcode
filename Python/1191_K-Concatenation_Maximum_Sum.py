# Author: Kaustav Ghosh
# Kadane's on single and double array; if total sum positive, add (k-2)*total

class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        def kadane(a):
            max_sum = 0
            cur = 0
            for x in a:
                cur = max(0, cur + x)
                max_sum = max(max_sum, cur)
            return max_sum

        total = sum(arr)
        if k == 1:
            return kadane(arr) % MOD
        two_max = kadane(arr + arr)
        if total > 0:
            return (two_max + (k - 2) * total) % MOD
        return two_max % MOD
