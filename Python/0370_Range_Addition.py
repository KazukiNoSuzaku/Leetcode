# You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].
# You have an array arr of length initialized to all zeros, and you have some operations to apply.
# For each operation updates[i], you should add the increment inc to all the elements
# arr[startIdx] through arr[endIdx] (inclusive).
# Return arr after applying all the updates.

# Example 1:
# Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
# Output: [-2,0,3,5,3]

# Constraints:
# 1 <= length <= 10^5
# 0 <= updates.length <= 10^4

# Author: Kaustav Ghosh

class Solution(object):
    def getModifiedArray(self, length, updates):
        diff = [0] * (length + 1)
        for start, end, inc in updates:
            diff[start] += inc
            diff[end + 1] -= inc
        res = []
        prefix = 0
        for i in range(length):
            prefix += diff[i]
            res.append(prefix)
        return res
