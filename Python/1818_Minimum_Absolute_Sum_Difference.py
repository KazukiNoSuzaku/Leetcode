# Author: Kaustav Ghosh

class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        import bisect
        MOD = 10 ** 9 + 7
        sorted1 = sorted(nums1)
        total = 0
        n = len(nums1)
        diffs = []
        for i in range(n):
            d = abs(nums1[i] - nums2[i])
            total += d
            diffs.append(d)
        best_save = 0
        for i in range(n):
            if diffs[i] == 0:
                continue
            # Find closest value in nums1 to nums2[i]
            idx = bisect.bisect_left(sorted1, nums2[i])
            if idx < n:
                best_save = max(best_save, diffs[i] - abs(sorted1[idx] - nums2[i]))
            if idx > 0:
                best_save = max(best_save, diffs[i] - abs(sorted1[idx - 1] - nums2[i]))
        return (total - best_save) % MOD
