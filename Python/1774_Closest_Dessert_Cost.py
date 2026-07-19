# Author: Kaustav Ghosh
# Problem: Closest Dessert Cost
# Approach: For each base flavor, enumerate every topping combination (0/1/2 of each) and keep the total closest to target, breaking ties toward the smaller cost

class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        self.best = float('inf')

        def better(cost):
            if (abs(cost - target) < abs(self.best - target)
                    or (abs(cost - target) == abs(self.best - target) and cost < self.best)):
                self.best = cost

        def choose(i, cost):
            better(cost)
            if i == len(toppingCosts):
                return
            for count in range(3):  # 0, 1, or 2 of this topping
                choose(i + 1, cost + count * toppingCosts[i])

        for base in baseCosts:
            choose(0, base)

        return self.best
