# Author: Kaustav Ghosh
# Problem: Find Missing Observations
# Approach: Fixing the mean over all the rolls fixes their total exactly, so the missing rolls must sum to that total minus what the known rolls already contribute. That target is reachable only if it lies between the smallest and largest sums the missing dice could produce, namely one and six per die, and otherwise no answer exists at all. When it is reachable, spreading the target as evenly as possible always works: every die takes the floor of the share, and the leftover is handed out one extra pip at a time, which keeps every value within a legal die face.

class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        needed = mean * (n + len(rolls)) - sum(rolls)
        if needed < n or needed > 6 * n:
            return []
        share = needed // n
        leftover = needed % n
        return [share + 1] * leftover + [share] * (n - leftover)
