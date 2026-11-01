# Author: Kaustav Ghosh
# Problem: Closest Dessert Cost
# Approach: Bases and toppings are independent: exactly one base is chosen, while each of the at most ten toppings is taken zero, one or two times. The reachable topping totals are built up by growing a set one topping at a time, which collapses the three to the tenth choice sequences down to the distinct sums they actually produce, and every base is then added to every such sum. The comparison keeps the candidate with the smaller gap and, on a tie, the cheaper dessert, matching the problem's tie-break.

class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        extras = {0}
        for cost in toppingCosts:
            extras = {total + take * cost for total in extras for take in (0, 1, 2)}

        best = None
        for base in baseCosts:
            for extra in extras:
                cost = base + extra
                if best is None:
                    best = cost
                    continue
                gap, best_gap = abs(cost - target), abs(best - target)
                if gap < best_gap or (gap == best_gap and cost < best):
                    best = cost
        return best
