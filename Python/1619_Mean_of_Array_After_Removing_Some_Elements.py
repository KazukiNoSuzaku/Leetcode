# Author: Kaustav Ghosh
# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        n = len(arr)
        trim = n // 20  # 5%
        return sum(arr[trim:n - trim]) / float(n - 2 * trim)
