# Author: Kaustav Ghosh
# Problem: Minimum Time to Make Rope Colorful
# Approach: For each run of same-colored balloons, keep the costliest and remove the rest, so add (run sum - run max)

class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        total = 0
        i, n = 0, len(colors)
        while i < n:
            j = i
            run_sum = run_max = 0
            while j < n and colors[j] == colors[i]:
                run_sum += neededTime[j]
                run_max = max(run_max, neededTime[j])
                j += 1
            total += run_sum - run_max
            i = j
        return total
