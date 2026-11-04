# Author: Kaustav Ghosh
# Problem: Maximum Value at a Given Index in a Bounded Array
# Approach: For a chosen peak the cheapest array that is still valid steps down by one on each side until it bottoms out at 1 and stays there, so the smallest possible total for that peak is a closed-form sum of an arithmetic run plus a tail of ones. That total only grows as the peak grows, which makes the condition monotone and the answer the largest peak whose minimum total still fits inside maxSum, found by binary search. Everything is integer arithmetic, so the billion-scale bounds never lose precision.

class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def side(peak, length):
            # Cheapest total for `length` cells beside the peak: peak - 1, peak - 2,
            # ... and then 1 once the descent would drop below it.
            if length <= 0:
                return 0
            if peak - 1 >= length:
                top, bottom = peak - 1, peak - length
                return (top + bottom) * length // 2
            descent = peak - 1
            return descent * (descent + 1) // 2 + (length - descent)

        def total(peak):
            return peak + side(peak, index) + side(peak, n - 1 - index)

        low, high = 1, maxSum
        while low < high:
            middle = (low + high + 1) // 2
            if total(middle) <= maxSum:
                low = middle
            else:
                high = middle - 1
        return low
