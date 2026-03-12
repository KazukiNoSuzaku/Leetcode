# Author: Kaustav Ghosh
# Extract digits, compute product minus sum

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = [int(d) for d in str(n)]
        product = 1
        for d in digits:
            product *= d
        return product - sum(digits)
