# Author: Kaustav Ghosh
# Problem: Abbreviating the Product of a Range
# Approach: Compute the exact product with Python big integers, strip and count the trailing zeros as C, and take the remaining significant digits. If at most 10 significant digits remain, show them all; otherwise show the first five, an ellipsis, and the last five, followed by eC

class Solution(object):
    def abbreviateProduct(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: str
        """
        product = 1
        for x in range(left, right + 1):
            product *= x

        s = str(product)
        significant = s.rstrip('0')
        zeros = len(s) - len(significant)

        if len(significant) <= 10:
            return significant + 'e' + str(zeros)
        return significant[:5] + '...' + significant[-5:] + 'e' + str(zeros)
