# Author: Kaustav Ghosh
# Problem: Maximum Number of Ways to Partition an Array
# Approach: A pivot p is valid when 2*prefix[p] == total. Changing element i by d=k-nums[i] shifts the condition: pivots left of/at i need 2*prefix==total+d, pivots right of i need 2*prefix==total-d. Sweep i keeping running counts of prefix values on each side and take the best over no-change and every single change

from collections import Counter

class Solution(object):
    def waysToPartition(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        total = prefix[n - 1]

        # pivot boundaries p = 1..n-1 correspond to prefix[p-1]
        pivot_sums = [prefix[p] for p in range(0, n - 1)]  # left-sum if we cut after index p

        base = sum(1 for s in pivot_sums if 2 * s == total)
        best = base

        right = Counter(pivot_sums)
        left = Counter()
        for i in range(n):
            if i >= 1:
                # boundary using prefix[i-1] moves from right to left
                right[prefix[i - 1]] -= 1
                left[prefix[i - 1]] += 1
            d = k - nums[i]
            need_left_side = total + d   # boundaries at/left of i
            need_right_side = total - d  # boundaries right of i
            cnt = 0
            if need_left_side % 2 == 0:
                cnt += left[need_left_side // 2]
            if need_right_side % 2 == 0:
                cnt += right[need_right_side // 2]
            best = max(best, cnt)
        return best
