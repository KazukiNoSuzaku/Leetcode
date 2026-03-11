# Send n people to city A and n to city B minimizing total cost.
# costs[i] = [costA, costB].

# Author: Kaustav Ghosh

class Solution(object):
    def twoCitySchedCost(self, costs):
        # Sort by difference (costA - costB): cheapest to send to A first
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        return sum(costs[i][0] for i in range(n)) + sum(costs[i][1] for i in range(n, 2*n))
