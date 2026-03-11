# Minimum swaps to arrange couples side by side on a bench.

# Author: Kaustav Ghosh

class Solution(object):
    def minSwapsCouples(self, row):
        pos = {v: i for i, v in enumerate(row)}
        swaps = 0
        for i in range(0, len(row), 2):
            partner = row[i] ^ 1
            if row[i + 1] != partner:
                j = pos[partner]
                pos[row[i + 1]] = j
                row[i + 1], row[j] = row[j], row[i + 1]
                swaps += 1
        return swaps
