# Author: Kaustav Ghosh

class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        self.best = baseCosts[0]

        def dfs(idx, current):
            if abs(current - target) < abs(self.best - target) or \
               (abs(current - target) == abs(self.best - target) and current < self.best):
                self.best = current
            if idx == len(toppingCosts) or current > target:
                return
            dfs(idx + 1, current)
            dfs(idx + 1, current + toppingCosts[idx])
            dfs(idx + 1, current + 2 * toppingCosts[idx])

        for base in baseCosts:
            dfs(0, base)
        return self.best
