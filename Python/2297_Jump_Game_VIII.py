# Author: Kaustav Ghosh
# Problem: 2297. Jump Game VIII
# URL: https://leetcode.com/problems/jump-game-viii/
# Difficulty: Medium
# Premium: True
#
# Approach:
# Use two monotone stacks to build edges: one decreasing stack for next greater
# or equal element (costs[i] applied), one increasing stack for next smaller
# element (costs[i] applied). Then run DP from index 0 to n-1.
#
# def minCost(nums, costs):
#     n = len(nums)
#     INF = float('inf')
#     dp = [INF] * n
#     dp[0] = 0
#     # Build adjacency: for each i, find the set of j's reachable
#     # Stack for next >= (decreasing stack of values)
#     dec_stack = []  # indices, monotone decreasing by value
#     inc_stack = []  # indices, monotone increasing by value
#     for i in range(n):
#         while dec_stack and nums[dec_stack[-1]] <= nums[i]:
#             j = dec_stack.pop()
#             dp[i] = min(dp[i], dp[j] + costs[i])
#         dec_stack.append(i)
#         while inc_stack and nums[inc_stack[-1]] > nums[i]:
#             j = inc_stack.pop()
#             dp[i] = min(dp[i], dp[j] + costs[i])
#         inc_stack.append(i)
#     return dp[n - 1]

class Solution(object):
    pass
