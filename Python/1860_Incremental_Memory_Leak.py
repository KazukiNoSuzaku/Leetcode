# Author: Kaustav Ghosh
# Problem: Incremental Memory Leak
# Approach: Each second i allocates i bits to the larger stick (stick 1 on a tie); simulate until neither can hold the next allocation, then report the crash time and remaining memory

class Solution(object):
    def memLeak(self, memory1, memory2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """
        i = 1
        while memory1 >= i or memory2 >= i:
            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i
            i += 1
        return [i, memory1, memory2]
