# Author: Kaustav Ghosh
# Problem: Partition Array Into Two Arrays to Minimize Sum Difference
# Approach: Split the 2n elements into two halves. One partition takes i elements from the left half and n-i from the right. Meet in the middle: enumerate subset sums per chosen count in each half, then for each left-subset sum binary search the right half for the complementary sum closest to total/2

import bisect

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 2
        total = sum(nums)
        left, right = nums[:n], nums[n:]

        def subset_sums_by_count(arr):
            m = len(arr)
            groups = [[] for _ in range(m + 1)]
            for mask in range(1 << m):
                bits = bin(mask).count('1')
                s = sum(arr[j] for j in range(m) if mask >> j & 1)
                groups[bits].append(s)
            return groups

        left_groups = subset_sums_by_count(left)
        right_groups = subset_sums_by_count(right)
        for g in right_groups:
            g.sort()

        best = float('inf')
        for i in range(n + 1):
            rights = right_groups[n - i]
            for a in left_groups[i]:
                # minimize |total - 2*(a+b)| = |(total-2a) - 2b|
                target = (total - 2 * a) / 2.0
                pos = bisect.bisect_left(rights, target)
                for p in (pos - 1, pos):
                    if 0 <= p < len(rights):
                        best = min(best, abs(total - 2 * (a + rights[p])))
        return best
