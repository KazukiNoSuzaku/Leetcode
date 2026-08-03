# Author: Kaustav Ghosh
# Problem: Design Movie Rental System
# Approach: Keep a price lookup per (shop, movie), a sorted list of (price, shop) of unrented copies per movie, and a global sorted list of (price, shop, movie) for rented copies. Every operation is a sorted insert/remove or a top-5 slice

from sortedcontainers import SortedList

class MovieRentingSystem(object):

    def __init__(self, n, entries):
        """
        :type n: int
        :type entries: List[List[int]]
        """
        self.price = {}
        self.available = {}                 # movie -> SortedList of (price, shop)
        self.rented = SortedList()          # (price, shop, movie)
        for shop, movie, price in entries:
            self.price[(shop, movie)] = price
            self.available.setdefault(movie, SortedList()).add((price, shop))

    def search(self, movie):
        """
        :type movie: int
        :rtype: List[int]
        """
        sl = self.available.get(movie)
        if not sl:
            return []
        return [shop for _, shop in sl[:5]]

    def rent(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        price = self.price[(shop, movie)]
        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        price = self.price[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self):
        """
        :rtype: List[List[int]]
        """
        return [[shop, movie] for _, shop, movie in self.rented[:5]]
