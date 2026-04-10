# Author: Kaustav Ghosh
# Problem: 2247. Maximum Cost of Trip With K Highways
# URL: https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/
# Difficulty: Hard
# Note: Premium problem
#
# Approach:
# Bitmask DP on visited nodes. dp[mask][i] = max cost of a path visiting
# exactly the nodes in mask and ending at node i, using edges from highways.
# Answer is max dp[mask][i] where popcount(mask) == k + 1.

class Solution(object):
    pass
