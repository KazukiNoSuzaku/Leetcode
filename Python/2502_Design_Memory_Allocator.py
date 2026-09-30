# Author: Kaustav Ghosh
# Problem: Design Memory Allocator
# Approach: Hold the memory as one array of owner ids, zero meaning free. Allocation scans left to right for the first run of free units long enough and stamps it with the id, while freeing sweeps the array clearing every unit that id owns. The limits are small enough that a direct scan per call is comfortable

class Allocator(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.memory = [0] * n

    def allocate(self, size, mID):
        """
        :type size: int
        :type mID: int
        :rtype: int
        """
        free_run = 0
        for i, owner in enumerate(self.memory):
            free_run = free_run + 1 if owner == 0 else 0
            if free_run == size:
                start = i - size + 1
                for j in range(start, i + 1):
                    self.memory[j] = mID
                return start
        return -1

    def freeMemory(self, mID):
        """
        :type mID: int
        :rtype: int
        """
        freed = 0
        for i, owner in enumerate(self.memory):
            if owner == mID:
                self.memory[i] = 0
                freed += 1
        return freed
