# Author: Kaustav Ghosh
# Problem: Find the Index of the Large Integer
# Approach: Halve the search range each step. Comparing the leftmost half against the rightmost half of equal size tells which side holds the odd large value, since equal-sized blocks of identical values have equal sums. When the range has odd length those two halves leave the middle element out, so an equal verdict pins the answer there. That is one call per halving, about 19 for the largest allowed array

# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation.
# class ArrayReader(object):
#    # Compares the sum of arr[l..r] with the sum of arr[x..y]
#    # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#    # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#    # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l, r, x, y):
#        """
#        :type l, r, x, y: int
#        :rtype int
#        """
#
#    # Returns the length of the array
#    def length(self):
#        """
#        :rtype int
#        """


class Solution(object):
    def getIndex(self, reader):
        """
        :type reader: ArrayReader
        :rtype: int
        """
        low, high = 0, reader.length() - 1
        while low < high:
            half = (high - low + 1) // 2
            verdict = reader.compareSub(low, low + half - 1, high - half + 1, high)
            if verdict > 0:
                high = low + half - 1
            elif verdict < 0:
                low = high - half + 1
            else:
                low = high = low + half
        return low
