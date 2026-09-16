# Author: Kaustav Ghosh
# Problem: Task Scheduler II
# Approach: Tasks must be finished in order, so walk them keeping the earliest day each type may run again. Each task takes the next day unless its type is still cooling down, in which case it waits for that day, and finishing it books its type out for the next space days

class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        """
        day = 0
        available = {}
        for task in tasks:
            day = max(day + 1, available.get(task, 0))
            available[task] = day + space + 1
        return day
