# Author: Kaustav Ghosh
# Problem: Find Minimum Time to Finish All Jobs II
# Approach: Each worker handles exactly one job. To minimize the slowest worker, pair the largest job with the fastest worker: sort both ascending and match by rank, then take the maximum ceil(job/worker) across pairs

class Solution(object):
    def minimumTime(self, jobs, workers):
        """
        :type jobs: List[int]
        :type workers: List[int]
        :rtype: int
        """
        jobs.sort()
        workers.sort()
        return max(-(-j // w) for j, w in zip(jobs, workers))
