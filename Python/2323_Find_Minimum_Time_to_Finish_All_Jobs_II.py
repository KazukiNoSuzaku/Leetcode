# Author: Kaustav Ghosh
# Problem: 2323. Find Minimum Time to Finish All Jobs II
# URL: https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/
# Difficulty: Medium
# Note: Premium problem
#
# Approach:
# Sort both jobs and workers arrays. Assign the largest job to the largest worker,
# second largest job to second largest worker, etc. The answer is the maximum of
# ceil(jobs[i] / workers[i]) over all i, since each worker i handles jobs[i] time units.

class Solution(object):
    def minimumTime(self, jobs, workers):
        """
        :type jobs: List[int]
        :type workers: List[int]
        :rtype: int
        """
        import math
        jobs.sort()
        workers.sort()
        ans = 0
        for j, w in zip(jobs, workers):
            ans = max(ans, math.ceil(j / float(w)))
        return ans
