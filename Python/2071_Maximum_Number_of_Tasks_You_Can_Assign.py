# Author: Kaustav Ghosh
# Problem 2071: Maximum Number of Tasks You Can Assign

from collections import deque
from bisect import bisect_right

class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        tasks.sort()
        workers.sort()

        def can_assign(k):
            # Try to assign the k easiest tasks using k strongest workers
            # Workers are workers[-k:]
            available = deque()
            w_idx = len(workers) - 1
            remaining_pills = pills
            task_list = tasks[:k]
            w_list = sorted(workers[-k:])

            # Use sorted multiset approach
            from sortedcontainers import SortedList
            w_sorted = SortedList(w_list)

            for i in range(k - 1, -1, -1):
                t = task_list[i]
                # Try to assign without pill first (strongest available)
                if w_sorted and w_sorted[-1] >= t:
                    # Check if we can use weakest sufficient worker
                    idx = w_sorted.bisect_left(t)
                    if idx < len(w_sorted):
                        w_sorted.pop(idx)
                    else:
                        return False
                elif remaining_pills > 0:
                    # Try with pill - find weakest worker >= t - strength
                    idx = w_sorted.bisect_left(t - strength)
                    if idx < len(w_sorted):
                        w_sorted.pop(idx)
                        remaining_pills -= 1
                    else:
                        return False
                else:
                    return False
            return True

        lo, hi = 0, min(len(tasks), len(workers))
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_assign(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
