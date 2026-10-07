# Author: Kaustav Ghosh
# Problem: Guess the Majority in a Hidden Array
# Approach: A query over four indices reports only their distribution, but holding three indices fixed and swapping the fourth reveals whether those two fourth values agree: the same triple with equal partners always yields the same verdict. So compare index 0 against every other index, always through a triple that excludes both, which the guaranteed five elements make possible. Counting agreements splits the array into the two values, and the larger side names the answer, or -1 on a tie. That costs about n calls, within the 2n budget

# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation.
# class ArrayReader(object):
#    # Compares 4 different elements in the array
#    # return 4 if the values of the 4 elements are the same (0 or 1).
#    # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#    # return 0 if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a, b, c, d):
#        """
#        :type a, b, c, d: int
#        :rtype int
#        """
#
#    # Returns the length of the array
#    def length(self):
#        """
#        :rtype int
#        """


class Solution(object):
    def guessMajority(self, reader):
        """
        :type reader: ArrayReader
        :rtype: int
        """
        n = reader.length()
        base_with_zero = reader.query(0, 1, 2, 3)
        base_without_zero = reader.query(1, 2, 3, 4)

        matches_zero = [True] * n
        matches_zero[1] = reader.query(0, 2, 3, 4) == base_without_zero
        matches_zero[2] = reader.query(0, 1, 3, 4) == base_without_zero
        matches_zero[3] = reader.query(0, 1, 2, 4) == base_without_zero
        matches_zero[4] = base_without_zero == base_with_zero
        for i in range(5, n):
            matches_zero[i] = reader.query(1, 2, 3, i) == base_with_zero

        same = sum(1 for flag in matches_zero if flag)
        other = n - same
        if same > other:
            return 0
        if other > same:
            return matches_zero.index(False)
        return -1
