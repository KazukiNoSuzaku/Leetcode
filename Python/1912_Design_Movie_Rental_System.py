# Author: Kaustav Ghosh
# https://leetcode.com/problems/design-movie-rental-system/

from collections import defaultdict
from sortedcontainers import SortedList

class MovieRentingSystem(object):

    def __init__(self, n, entries):
        """
        :type n: int
        :type entries: List[List[int]]
        """
        self.price = {}
        self.available = defaultdict(SortedList)  # movie -> SortedList of (price, shop)
        self.rented = SortedList()  # (price, shop, movie)
        for shop, movie, p in entries:
            self.price[(shop, movie)] = p
            self.available[movie].add((p, shop))

    def search(self, movie):
        """
        :type movie: int
        :rtype: List[int]
        """
        return [s for _, s in self.available[movie][:5]]

    def rent(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        p = self.price[(shop, movie)]
        self.available[movie].remove((p, shop))
        self.rented.add((p, shop, movie))

    def drop(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        p = self.price[(shop, movie)]
        self.rented.remove((p, shop, movie))
        self.available[movie].add((p, shop))

    def report(self):
        """
        :rtype: List[List[int]]
        """
        return [[s, m] for _, s, m in self.rented[:5]]
