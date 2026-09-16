# Author: Kaustav Ghosh
# Problem: Minimum Costs Using the Train Line
# Approach: Carry two running totals, the cheapest way to arrive at the current stop on the regular route and on the express route. Each hop either stays on its route or switches, where hopping onto the express costs expressCost and dropping back to the regular is free, so the answer for a stop is the smaller of the two totals

class Solution(object):
    def minimumCosts(self, regular, express, expressCost):
        """
        :type regular: List[int]
        :type express: List[int]
        :type expressCost: int
        :rtype: List[int]
        """
        on_regular = 0
        on_express = float('inf')
        costs = []
        for r, e in zip(regular, express):
            on_regular, on_express = (min(on_regular, on_express) + r,
                                      min(on_express, on_regular + expressCost) + e)
            costs.append(min(on_regular, on_express))
        return costs
