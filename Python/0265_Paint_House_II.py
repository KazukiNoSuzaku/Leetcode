# There is a row of n houses, where each house can be painted one of k colors.
# The cost of painting each house with a certain color is represented by an n x k cost matrix costs.
# No two adjacent houses can have the same color. Return the minimum cost.

# Example 1:
# Input: costs = [[1,5,3],[2,9,4]]
# Output: 5

# Constraints:
# costs.length == n
# costs[i].length == k
# 1 <= n <= 100
# 2 <= k <= 20
# 1 <= costs[i][j] <= 20

# Author: Kaustav Ghosh

class Solution(object):
    def minCostII(self, costs):
        if not costs:
            return 0
        n, k = len(costs), len(costs[0])
        min1 = min2 = float('inf')
        min1_idx = -1
        for j in range(k):
            if costs[0][j] < min1:
                min2 = min1
                min1 = costs[0][j]
                min1_idx = j
            elif costs[0][j] < min2:
                min2 = costs[0][j]
        for i in range(1, n):
            new_min1 = new_min2 = float('inf')
            new_min1_idx = -1
            for j in range(k):
                prev = min2 if j == min1_idx else min1
                cost = costs[i][j] + prev
                if cost < new_min1:
                    new_min2 = new_min1
                    new_min1 = cost
                    new_min1_idx = j
                elif cost < new_min2:
                    new_min2 = cost
            min1, min2, min1_idx = new_min1, new_min2, new_min1_idx
        return min1
