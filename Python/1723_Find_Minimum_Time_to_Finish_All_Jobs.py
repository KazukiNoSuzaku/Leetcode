# Author: Kaustav Ghosh
# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        jobs.sort(reverse=True)
        workers = [0] * k
        self.result = float('inf')

        def backtrack(idx):
            if idx == len(jobs):
                self.result = min(self.result, max(workers))
                return
            # Pruning: if current max already >= result, skip
            if max(workers) >= self.result:
                return
            seen = set()
            for i in range(k):
                if workers[i] in seen:
                    continue
                seen.add(workers[i])
                workers[i] += jobs[idx]
                backtrack(idx + 1)
                workers[i] -= jobs[idx]

        backtrack(0)
        return self.result
