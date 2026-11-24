# Author: Kaustav Ghosh
# Problem: Brightest Position on Street
# Approach: Brightness only changes where a lamp's lit interval begins or ends, so the whole street collapses to those boundary coordinates rather than the hundred million positions between them. Each lamp is recorded as one increment at the first position it lights and one decrement just past the last, and sweeping the boundaries in increasing order carries the running count of lamps covering the current stretch. Because the sweep runs left to right and the best is replaced only on a strict improvement, the first coordinate achieving the maximum is the one reported, which is exactly the smallest brightest position.

class Solution(object):
    def brightestPosition(self, lights):
        """
        :type lights: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        changes = defaultdict(int)
        for position, span in lights:
            changes[position - span] += 1
            changes[position + span + 1] -= 1

        best_position = 0
        brightest = 0
        covering = 0
        for point in sorted(changes):
            covering += changes[point]
            if covering > brightest:
                brightest = covering
                best_position = point
        return best_position
