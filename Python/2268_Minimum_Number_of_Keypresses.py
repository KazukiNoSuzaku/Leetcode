# Author: Kaustav Ghosh
# Problem: 2268. Minimum Number of Keypresses
# URL: https://leetcode.com/problems/minimum-number-of-keypresses/
# Difficulty: Medium
# Premium: True
#
# Approach:
# Count character frequencies, sort descending. The first 9 most frequent
# characters cost 1 press each, next 9 cost 2 presses, rest cost 3 presses.
#
# from collections import Counter
# def minimumKeypresses(s):
#     freqs = sorted(Counter(s).values(), reverse=True)
#     total = 0
#     for i, f in enumerate(freqs):
#         total += f * (i // 9 + 1)
#     return total

class Solution(object):
    pass
