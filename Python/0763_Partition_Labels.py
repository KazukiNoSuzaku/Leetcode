# Partition a string so each letter appears in at most one part; return part sizes.

# Author: Kaustav Ghosh

class Solution(object):
    def partitionLabels(self, s):
        last = {c: i for i, c in enumerate(s)}
        res = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
