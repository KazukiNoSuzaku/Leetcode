# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green.
# The cost of painting each house with a certain color is different.
# You have to paint all the houses such that no two adjacent houses have the same color.
# Return the minimum cost to paint all houses.

# Example 1:
# Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 blue, house 1 green, house 2 blue. Cost = 2 + 5 + 3 = 10.

# Constraints:
# costs.length == n
# costs[i].length == 3
# 1 <= n <= 100
# 1 <= costs[i][j] <= 20

# Author: Kaustav Ghosh

class Solution(object):
    def minCost(self, costs):
        r, g, b = 0, 0, 0
        for cr, cg, cb in costs:
            r, g, b = min(g, b) + cr, min(r, b) + cg, min(r, g) + cb
        return min(r, g, b)
