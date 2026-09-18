# Author: Kaustav Ghosh
# Problem: Longest Subsequence With Limited Sum
# Approach: Order does not matter for a sum, and the longest subsequence under a budget always takes the smallest values, so sort, build prefix sums and binary search each query for how many prefixes fit

from bisect import bisect_right
from itertools import accumulate


class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        prefix = list(accumulate(sorted(nums)))
        return [bisect_right(prefix, q) for q in queries]
