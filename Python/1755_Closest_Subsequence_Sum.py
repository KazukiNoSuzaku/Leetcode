# Author: Kaustav Ghosh

class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        import bisect
        n = len(nums)
        half = n // 2

        def get_all_sums(arr):
            sums = {0}
            for x in arr:
                sums = sums | {s + x for s in sums}
            return sorted(sums)

        left_sums = get_all_sums(nums[:half])
        right_sums = get_all_sums(nums[half:])
        res = abs(goal)
        for s in left_sums:
            target = goal - s
            idx = bisect.bisect_left(right_sums, target)
            if idx < len(right_sums):
                res = min(res, abs(target - right_sums[idx]))
            if idx > 0:
                res = min(res, abs(target - right_sums[idx - 1]))
        return res
