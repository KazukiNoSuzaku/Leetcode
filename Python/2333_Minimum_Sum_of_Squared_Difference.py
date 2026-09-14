# Author: Kaustav Ghosh
# Problem: Minimum Sum of Squared Difference
# Approach: Only the absolute differences matter and a change to either array shrinks a difference by one, so pool k = k1 + k2. If the total difference is at most k the answer is 0. Otherwise bucket-count the differences and greedily lower the largest level by level: moving a whole bucket down one costs its count, and if k runs out mid-level only k of them move

class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        if sum(diffs) <= k:
            return 0
        top = max(diffs)
        count = [0] * (top + 1)
        for d in diffs:
            count[d] += 1
        for d in range(top, 0, -1):
            if k >= count[d]:
                k -= count[d]
                count[d - 1] += count[d]
                count[d] = 0
            else:
                count[d] -= k
                count[d - 1] += k
                break
        return sum(d * d * c for d, c in enumerate(count))
