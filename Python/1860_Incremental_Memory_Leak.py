# Author: Kaustav Ghosh
# Problem 1860: Incremental Memory Leak

class Solution(object):
    def memLeak(self, memory1, memory2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """
        t = 1
        while t <= max(memory1, memory2):
            if memory1 >= memory2:
                memory1 -= t
            else:
                memory2 -= t
            t += 1
        return [t, memory1, memory2]
