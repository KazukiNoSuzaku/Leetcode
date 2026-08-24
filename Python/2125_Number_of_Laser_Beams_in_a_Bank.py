# Author: Kaustav Ghosh
# Problem: Number of Laser Beams in a Bank
# Approach: Beams connect devices on consecutive non-empty rows. Count devices per row, drop empty rows, and sum the product of adjacent counts

class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        counts = [row.count('1') for row in bank if row.count('1') > 0]
        return sum(counts[i] * counts[i + 1] for i in range(len(counts) - 1))
