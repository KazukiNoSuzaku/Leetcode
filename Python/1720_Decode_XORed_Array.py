# Author: Kaustav Ghosh
# Problem: Decode XORed Array
# Approach: Each encoded entry is the exclusive-or of two neighbouring originals, and exclusive-or is its own inverse, so applying an encoded value to the original just recovered yields the next one. With the first element given, the whole array unrolls in a single pass with no arithmetic beyond that.

class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        original = [first]
        for value in encoded:
            original.append(original[-1] ^ value)
        return original
