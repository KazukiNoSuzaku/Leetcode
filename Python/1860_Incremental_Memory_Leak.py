# Author: Kaustav Ghosh
# Problem: Incremental Memory Leak
# Approach: The rule is fully deterministic, so the process is simply played out: each second the larger stick gives up that second's allocation, with ties going to the first stick, and the loop ends the moment neither can cover it. Simulating is cheap despite the two-billion limits because the amount taken grows by one every second, so the seconds survived are on the order of the square root of the total memory, a few tens of thousands of iterations at most.

class Solution(object):
    def memLeak(self, memory1, memory2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """
        second = 1
        while memory1 >= second or memory2 >= second:
            if memory1 >= memory2:
                memory1 -= second
            else:
                memory2 -= second
            second += 1
        return [second, memory1, memory2]
