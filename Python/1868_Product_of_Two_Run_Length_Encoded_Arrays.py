# Author: Kaustav Ghosh
# Problem: Product of Two Run-Length Encoded Arrays
# Approach: The two encodings never have to be expanded: within the overlap of one segment from each, both values are constant, so the product is constant too and covers as many positions as the shorter remaining part of the two segments. Walking the pair of segment lists and consuming that many positions at a time therefore produces the product directly, with one step per segment boundary from either side. Merging a chunk into the previous output entry whenever the product repeats is what keeps the result at its minimum possible length, which matters because neighbouring chunks can easily share a product.

class Solution(object):
    def findRLEArray(self, encoded1, encoded2):
        """
        :type encoded1: List[List[int]]
        :type encoded2: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        j = 0
        remaining = encoded2[0][1]
        for value, frequency in encoded1:
            while frequency:
                taken = min(frequency, remaining)
                product = value * encoded2[j][0]
                if result and result[-1][0] == product:
                    result[-1][1] += taken
                else:
                    result.append([product, taken])
                frequency -= taken
                remaining -= taken
                if not remaining and j + 1 < len(encoded2):
                    j += 1
                    remaining = encoded2[j][1]
        return result
