# Check if a pyramid can be built given allowed triangle patterns.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        rules = defaultdict(list)
        for a, b, c in allowed:
            rules[(a, b)].append(c)
        def build(row):
            if len(row) == 1: return True
            return any(build(next_row) for next_row in get_rows(row, 0, ''))
        def get_rows(row, i, cur):
            if i == len(row) - 1:
                yield cur
            else:
                for c in rules[(row[i], row[i+1])]:
                    for result in get_rows(row, i+1, cur+c):
                        yield result
        return build(bottom)
