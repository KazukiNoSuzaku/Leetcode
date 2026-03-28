# Author: Kaustav Ghosh
# Problem: 2158. Amount of New Area Painted Each Day
# URL: https://leetcode.com/problems/amount-of-new-area-painted-each-day/
# Premium Problem
# Approach: Segment tree with lazy propagation or interval jump-pointer merging.
# For each day i with paint[i] = [start, end], count unpainted cells in [start, end)
# and mark them as painted. Use a "next unpainted" pointer array for O(n log n).
#
# jump[i] = next position >= i that is still unpainted
# For paint [l, r): walk from jump[l], count each unpainted cell, advance pointer.
# Use path compression on jump array to achieve amortized efficiency.

class Solution(object):
    pass
