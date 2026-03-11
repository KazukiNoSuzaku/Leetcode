# Maximize total profit assigning jobs to workers; each worker can do one job <= their ability.

# Author: Kaustav Ghosh

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        res = i = best = 0
        for w in worker:
            while i < len(jobs) and jobs[i][0] <= w:
                best = max(best, jobs[i][1])
                i += 1
            res += best
        return res
