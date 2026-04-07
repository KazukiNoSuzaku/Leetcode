# Author: Kaustav Ghosh
# Problem: 2222. Number of Ways to Select Buildings
# URL: https://leetcode.com/problems/number-of-ways-to-select-buildings/
# Difficulty: Medium
#
# Approach:
# Track prefix counts of 0s and 1s seen so far. When we see a '0', it can
# complete a '10' pair (using count of prior 1s) or a '010' triple (using
# count of prior '10' pairs). Similarly for '1' with '01' pairs. Use running
# tallies for single digits and pairs to count valid triples.

class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt0 = cnt1 = 0
        cnt01 = cnt10 = 0
        result = 0
        for c in s:
            if c == '0':
                result += cnt10
                cnt01 += cnt1
                cnt0 += 1
            else:
                result += cnt01
                cnt10 += cnt0
                cnt1 += 1
        return result
