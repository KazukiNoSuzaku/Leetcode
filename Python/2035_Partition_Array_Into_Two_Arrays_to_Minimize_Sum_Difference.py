# Author: Kaustav Ghosh
# Problem 2035: Partition Array Into Two Arrays to Minimize Sum Difference

from itertools import combinations
from bisect import bisect_left

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 2
        total = sum(nums)
        left = nums[:n]
        right = nums[n:]
        # Meet in the middle
        # For each half, compute all possible subset sums grouped by size
        def get_sums(arr):
            m = len(arr)
            result = {}
            for k in range(m + 1):
                result[k] = []
                for combo in combinations(range(m), k):
                    s = sum(arr[i] for i in combo)
                    result[k].append(s)
                result[k].sort()
            return result

        left_sums = get_sums(left)
        right_sums = get_sums(right)

        ans = float('inf')
        for k in range(n + 1):
            # Pick k elements from left, n-k from right
            l_list = left_sums[k]
            r_list = right_sums[n - k]
            for ls in l_list:
                # sum of picked = ls + rs, sum of rest = total - ls - rs
                # diff = |2*(ls+rs) - total|, minimize
                target = total - 2 * ls
                # find rs closest to target/2
                idx = bisect_left(r_list, target // 2)
                for i in [idx - 1, idx]:
                    if 0 <= i < len(r_list):
                        rs = r_list[i]
                        diff = abs(total - 2 * (ls + rs))
                        ans = min(ans, diff)
        return ans
