# Author: Kaustav Ghosh
# Problem: Longer Contiguous Segments of Ones than Zeros
# Approach: Splitting the string on zeros leaves exactly the runs of ones, and splitting on ones leaves the runs of zeros, so the longest run of each digit is the longest piece of the corresponding split. A digit that never appears needs no special case: the split then yields only empty pieces, whose length is zero, which is already the right answer for it.

class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        longest_ones = max(len(run) for run in s.split("0"))
        longest_zeros = max(len(run) for run in s.split("1"))
        return longest_ones > longest_zeros
