# Given an array of integers citations where citations[i] is the number of citations a researcher
# received for their ith paper, and citations is sorted in ascending order, return the researcher's h-index.
# The h-index is defined as the maximum value of h such that the researcher has published at least
# h papers that have each been cited at least h times.
# Design and implement an algorithm that runs in logarithmic time.

# Example 1:
# Input: citations = [0,1,3,5,6]
# Output: 3

# Example 2:
# Input: citations = [1,2,100]
# Output: 2

# Constraints:
# n == citations.length
# 1 <= n <= 10^5
# 0 <= citations[i] <= 1000
# citations is sorted in ascending order.

# Author: Kaustav Ghosh

class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if citations[n - mid] >= mid:
                lo = mid
            else:
                hi = mid - 1
        return lo
