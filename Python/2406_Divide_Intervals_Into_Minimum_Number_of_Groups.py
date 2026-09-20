# Author: Kaustav Ghosh
# Problem: Divide Intervals Into Minimum Number of Groups
# Approach: Two intervals clash only when they overlap, so the answer is the largest number of intervals covering a single point. Sort the starts and ends separately and sweep the starts, dropping every interval that already ended; the biggest number still open is the number of groups needed

class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        starts = sorted(interval[0] for interval in intervals)
        ends = sorted(interval[1] for interval in intervals)
        finished = 0
        best = 0
        for i, start in enumerate(starts):
            while ends[finished] < start:
                finished += 1
            best = max(best, i - finished + 1)
        return best
