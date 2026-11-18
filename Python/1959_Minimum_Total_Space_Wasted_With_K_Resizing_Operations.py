# Author: Kaustav Ghosh
# Problem: Minimum Total Space Wasted With K Resizing Operations
# Approach: Allowing k resizes means cutting the timeline into at most k + 1 contiguous stretches, each held at one size, and the best size for a stretch is its own maximum since anything smaller fails to fit; so a stretch's waste is its length times its maximum minus its sum. That makes this a partition problem, and I run a dynamic program over the number of stretches used and the prefix covered: the cost of ending a stretch at month i is the best cost of covering everything before its start plus that stretch's waste. Scanning each candidate start downwards lets the stretch's maximum and sum be carried along instead of recomputed, so each of the k + 1 rounds costs O(n^2) and the whole thing is O(k * n^2), which is small for the two hundred months allowed. Waste can never be negative, so once a round reaches zero no further stretch can improve on it and the rounds stop early, which is what happens as soon as enough resizes are allowed to give every month its own size.

class Solution(object):
    def minSpaceWastedKResizing(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        months = len(nums)
        stretches = min(k + 1, months)
        huge = float("inf")

        best = [huge] * (months + 1)
        best[0] = 0
        for _ in range(stretches):
            fresh = [huge] * (months + 1)
            for end in range(1, months + 1):
                tallest = 0
                used = 0
                for start in range(end - 1, -1, -1):
                    if nums[start] > tallest:
                        tallest = nums[start]
                    used += nums[start]
                    if best[start] == huge:
                        continue
                    value = best[start] + tallest * (end - start) - used
                    if value < fresh[end]:
                        fresh[end] = value
            best = [min(a, b) for a, b in zip(best, fresh)]
            if best[months] == 0:
                break

        return best[months]
