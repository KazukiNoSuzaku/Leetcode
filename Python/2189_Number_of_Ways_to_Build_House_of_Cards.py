# Author: Kaustav Ghosh
# 2189. Number of Ways to Build House of Cards
# https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/
# Difficulty: Medium (Premium)
#
# PREMIUM PROBLEM - Full description not publicly available.
#
# Approach (conceptual): DP on number of cards.
# A row of k triangles uses 2k cards for the triangles plus (k-1) horizontal
# cards = 3k - 1 cards total per row (for k >= 1).
# dp[n] = number of ways to use exactly n cards to build house of cards.
# For each row size k (k >= 1, 3k-1 <= n), if we place k triangles at bottom:
#   dp[n] += dp[n - (3k - 1)]  with each row having strictly fewer triangles
#            than the row below it.
# Use memoization with (remaining_cards, min_triangles_needed) state.
# Time: O(n * sqrt(n)), Space: O(n * sqrt(n))

class Solution(object):
    pass
