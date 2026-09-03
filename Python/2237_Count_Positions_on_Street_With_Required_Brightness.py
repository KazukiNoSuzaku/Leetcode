# Author: Kaustav Ghosh
# Problem: Count Positions on Street With Required Brightness
# Approach: Each light adds one unit of brightness over a clamped interval, so use a difference array to accumulate all intervals in one prefix pass. Then count positions whose brightness meets or exceeds their requirement

class Solution(object):
    def meetRequirement(self, n, lights, requirement):
        """
        :type n: int
        :type lights: List[List[int]]
        :type requirement: List[int]
        :rtype: int
        """
        diff = [0] * (n + 1)
        for pos, rng in lights:
            lo = max(0, pos - rng)
            hi = min(n - 1, pos + rng)
            diff[lo] += 1
            diff[hi + 1] -= 1

        brightness = 0
        count = 0
        for i in range(n):
            brightness += diff[i]
            if brightness >= requirement[i]:
                count += 1
        return count
