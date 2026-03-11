# Given pairs, find the longest chain where each pair starts after the previous ends.

# Author: Kaustav Ghosh

class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])
        cur_end = float('-inf')
        count = 0
        for a, b in pairs:
            if a > cur_end:
                cur_end = b
                count += 1
        return count
