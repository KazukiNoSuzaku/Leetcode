# Author: Kaustav Ghosh
# Problem: Minimum Adjacent Swaps for K Consecutive Ones
# Approach: Take positions of the ones and subtract their index (so a target block becomes "all equal"); for each k-window the cost of gathering to the median is a closed-form using prefix sums

class Solution(object):
    def minMoves(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ones = [i for i, x in enumerate(nums) if x == 1]
        n = len(ones)
        for i in range(n):
            ones[i] -= i  # normalize so consecutive target => equal values

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + ones[i]

        best = float('inf')
        for i in range(n - k + 1):
            mid = i + k // 2
            median = ones[mid]
            left_cnt = mid - i
            left_sum = prefix[mid] - prefix[i]
            right_cnt = i + k - mid - 1
            right_sum = prefix[i + k] - prefix[mid + 1]
            cost = (median * left_cnt - left_sum) + (right_sum - median * right_cnt)
            best = min(best, cost)
        return best
