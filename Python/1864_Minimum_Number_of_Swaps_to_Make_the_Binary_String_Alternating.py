# Author: Kaustav Ghosh
# Problem: Minimum Number of Swaps to Make the Binary String Alternating
# Approach: Counts of 0s and 1s decide which alternating targets are even possible; for each feasible target, the swaps needed are the number of misplaced ones (a swap fixes two positions)

class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = s.count('1')
        zeros = len(s) - ones

        def cost(start):
            # target has `start` at even indices, alternating after
            wrong_ones = sum(1 for i, c in enumerate(s)
                             if c == '1' and (i % 2 == 0) != (start == '1'))
            return wrong_ones

        # If counts differ by more than one, no alternating string exists
        if abs(ones - zeros) > 1:
            return -1
        if ones > zeros:
            return cost('1')          # must start with 1
        if zeros > ones:
            return cost('0')          # must start with 0
        return min(cost('0'), cost('1'))
