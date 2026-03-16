# Author: Kaustav Ghosh
# Problem: Apply Discount Every n Orders
# Approach: Track customer visit count, apply discount every n-th order

class Solution(object):
    pass

class Cashier(object):

    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        self.n = n
        self.discount = discount
        self.price_map = dict(zip(products, prices))
        self.count = 0

    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        self.count += 1
        total = sum(self.price_map[p] * a for p, a in zip(product, amount))
        if self.count % self.n == 0:
            total *= (100 - self.discount) / 100.0
        return total
