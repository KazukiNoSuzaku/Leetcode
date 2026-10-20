# Author: Kaustav Ghosh
# Problem: Get Maximum in Generated Array
# Approach: The array is defined purely by recurrence on earlier entries, so filling it left to right is enough and the maximum can be tracked as each entry is written rather than scanned for afterwards. The only care needed is the two base cases and the zero case, where the array has a single element and no maximum beyond it.

class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        values = [0] * (n + 1)
        values[1] = 1
        largest = 1
        for i in range(2, n + 1):
            half = i // 2
            values[i] = values[half] if i % 2 == 0 else values[half] + values[half + 1]
            if values[i] > largest:
                largest = values[i]
        return largest
