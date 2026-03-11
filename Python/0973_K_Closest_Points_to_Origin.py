# Given a list of points, return the k closest to the origin.

# Author: Kaustav Ghosh

import heapq

class Solution(object):
    def kClosest(self, points, k):
        return heapq.nsmallest(k, points, key=lambda p: p[0]*p[0] + p[1]*p[1])
