# Author: Kaustav Ghosh
# Problem: Number of Times Binary String Is Prefix-Aligned
# Approach: Track max flipped bit, count when max equals current step

class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        max_val = 0
        count = 0
        for i, f in enumerate(flips):
            max_val = max(max_val, f)
            if max_val == i + 1:
                count += 1
        return count
