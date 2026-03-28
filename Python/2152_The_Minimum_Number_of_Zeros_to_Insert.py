# Author: Kaustav Ghosh
# Problem: 2152. The Minimum Number of Zeros to Insert
# URL: https://leetcode.com/problems/the-minimum-number-of-zeros-to-insert/
# Premium Problem
# Approach: Greedy - track current nesting depth, insert zeros to balance parentheses
#
# SQL/Algorithm description:
# Given a binary string, we need to insert zeros to make every '1' preceded by
# an even number of zeros. We track the depth of open brackets and greedily
# determine the minimum zeros needed so that valid insertion can happen.
#
# For each character:
#   - If '(', increase open count
#   - If ')', decrease open count; if it drops below 0, we need to insert a zero pair
# The answer is the number of insertions needed.

class Solution(object):
    pass
