# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appears in both list1 and list2.

# Author: Kaustav Ghosh

class Solution(object):
    def findRestaurant(self, list1, list2):
        idx1 = {v: i for i, v in enumerate(list1)}
        best = float('inf')
        res = []
        for j, v in enumerate(list2):
            if v in idx1:
                s = idx1[v] + j
                if s < best:
                    best = s
                    res = [v]
                elif s == best:
                    res.append(v)
        return res
