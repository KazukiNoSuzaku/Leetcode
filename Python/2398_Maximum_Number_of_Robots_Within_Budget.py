# Author: Kaustav Ghosh
# Problem: Maximum Number of Robots Within Budget
# Approach: Adding a robot to a window never lowers its cost max(charge) + k * sum(running), so a two-pointer sliding window works: grow on the right and shrink from the left while over budget. A monotonic deque of indices with decreasing charge times gives the window maximum in O(1)

from collections import deque


class Solution(object):
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        """
        :type chargeTimes: List[int]
        :type runningCosts: List[int]
        :type budget: int
        :rtype: int
        """
        window_max = deque()
        left = 0
        running = 0
        best = 0
        for right, charge in enumerate(chargeTimes):
            while window_max and chargeTimes[window_max[-1]] <= charge:
                window_max.pop()
            window_max.append(right)
            running += runningCosts[right]
            while window_max and chargeTimes[window_max[0]] + (right - left + 1) * running > budget:
                if window_max[0] == left:
                    window_max.popleft()
                running -= runningCosts[left]
                left += 1
            best = max(best, right - left + 1)
        return best
