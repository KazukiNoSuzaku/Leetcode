# Author: Kaustav Ghosh
# Problem: Find Minimum Time to Finish All Jobs
# Approach: Whether a given ceiling on each worker's load is achievable gets easier as the ceiling rises, so the answer is found by binary search over the ceiling with a feasibility test underneath. The test assigns jobs to workers by backtracking, made tractable by three prunings: the jobs are tried largest first so that hopeless branches fail immediately; a worker whose load already matches one already tried is skipped, since the outcome would be identical; and when a job lands on an untouched worker no further untouched worker need be tried, because they are interchangeable. The search range runs from the largest single job, which no ceiling can go below, up to the total, which one worker could absorb alone.

class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        ordered = sorted(jobs, reverse=True)
        n = len(ordered)

        def feasible(ceiling):
            loads = [0] * k

            def place(index):
                if index == n:
                    return True
                job = ordered[index]
                tried = set()
                for worker in range(k):
                    load = loads[worker]
                    if load + job > ceiling or load in tried:
                        continue
                    tried.add(load)
                    loads[worker] = load + job
                    if place(index + 1):
                        return True
                    loads[worker] = load
                    if load == 0:
                        # Untouched workers are interchangeable.
                        break
                return False

            return place(0)

        low, high = max(ordered), sum(ordered)
        while low < high:
            middle = (low + high) // 2
            if feasible(middle):
                high = middle
            else:
                low = middle + 1
        return low
