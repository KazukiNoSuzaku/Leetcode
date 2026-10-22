# Author: Kaustav Ghosh
# Problem: Minimum Initial Energy to Finish Tasks
# Approach: The order is free, and what makes a task awkward is the gap between the energy it demands to begin and the energy it actually consumes, because that gap is headroom which must be present but is not spent. Tasks with a large gap should therefore be attempted while plenty of energy remains, that is early, so sorting by that gap ascending and then accumulating from the end gives the right order. The requirement is then built backwards: the energy needed before a task is whichever is larger of its own minimum, or its cost plus whatever the tasks after it already need.

class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        needed = 0
        for actual, minimum in sorted(tasks, key=lambda task: task[1] - task[0]):
            after = needed + actual
            needed = after if after > minimum else minimum
        return needed
