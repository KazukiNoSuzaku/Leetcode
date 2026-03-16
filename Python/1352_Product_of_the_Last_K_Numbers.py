# Author: Kaustav Ghosh
# Problem: Product of the Last K Numbers
# Approach: Prefix products list, reset on zero

class Solution(object):
    pass

class ProductOfNumbers(object):

    def __init__(self):
        self.prefix = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]
