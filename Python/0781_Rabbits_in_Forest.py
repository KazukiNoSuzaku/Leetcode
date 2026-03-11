# Find minimum number of rabbits in a forest given answers about same-color rabbits.

# Author: Kaustav Ghosh

from collections import Counter
import math

class Solution(object):
    def numRabbits(self, answers):
        count = Counter(answers)
        total = 0
        for ans, cnt in count.items():
            group_size = ans + 1
            total += math.ceil(cnt / float(group_size)) * group_size
        return total
