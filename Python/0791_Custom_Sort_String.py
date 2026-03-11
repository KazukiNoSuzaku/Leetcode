# Sort string s so characters present in order appear in that order.

# Author: Kaustav Ghosh

class Solution(object):
    def customSortString(self, order, s):
        rank = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda c: rank.get(c, len(order))))
