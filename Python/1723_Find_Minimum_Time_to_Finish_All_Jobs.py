# Author: Kaustav Ghosh
# Problem: Find Minimum Time to Finish All Jobs
# Approach: Backtrack assigning the biggest jobs first; prune any worker whose load would already reach the best answer, and skip workers with duplicate loads since those branches are symmetric

class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        jobs.sort(reverse=True)
        n = len(jobs)
        loads = [0] * k
        best = [sum(jobs)]

        def backtrack(i):
            if i == n:
                best[0] = min(best[0], max(loads))
                return
            seen = set()
            for w in range(k):
                if loads[w] in seen:
                    continue  # symmetric to an earlier worker
                seen.add(loads[w])
                if loads[w] + jobs[i] >= best[0]:
                    continue  # cannot beat the current best
                loads[w] += jobs[i]
                backtrack(i + 1)
                loads[w] -= jobs[i]

        backtrack(0)
        return best[0]
