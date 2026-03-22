# Author: Kaustav Ghosh

class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def calc_sum(val, count):
            if val >= count:
                return val * count - count * (count - 1) // 2
            return val * (val + 1) // 2 + (count - val)

        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            total = calc_sum(mid, index + 1) + calc_sum(mid, n - index) - mid
            if total <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left
