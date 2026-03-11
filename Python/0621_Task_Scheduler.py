# Given a list of tasks and cooldown n, find minimum intervals to finish all tasks.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        counts = sorted(Counter(tasks).values(), reverse=True)
        max_count = counts[0]
        max_count_tasks = counts.count(max_count)
        return max((max_count - 1) * (n + 1) + max_count_tasks, len(tasks))
