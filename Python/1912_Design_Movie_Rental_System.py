# Author: Kaustav Ghosh
# Problem: Design Movie Rental System
# Approach: Both queries want only the five cheapest entries, so each is served from a heap rather than a sorted structure: one heap of unrented copies per movie, keyed by price then shop, and one global heap of rented copies keyed by price, shop and movie. Renting and dropping do not touch the heaps they leave behind; the stale entry is simply skipped and discarded the next time it surfaces, because the opposite operation pushes a fresh copy. That lazy approach means an entry can legitimately appear twice in a heap if it was rented and dropped without a query in between, so both queries also skip anything they have already emitted. Only five entries are ever withdrawn and pushed back per query, which keeps each call logarithmic in the number of entries instead of linear.

class MovieRentingSystem(object):

    def __init__(self, n, entries):
        """
        :type n: int
        :type entries: List[List[int]]
        """
        from collections import defaultdict
        from heapq import heappush

        self.cost = {}
        self.unrented = defaultdict(list)
        self.rented = []
        self.out = set()
        for shop, movie, price in entries:
            self.cost[(shop, movie)] = price
            heappush(self.unrented[movie], (price, shop))

    def search(self, movie):
        """
        :type movie: int
        :rtype: List[int]
        """
        from heapq import heappop, heappush

        heap = self.unrented[movie]
        found = []
        seen = set()
        while heap and len(found) < 5:
            price, shop = heappop(heap)
            if (shop, movie) in self.out or shop in seen:
                continue
            seen.add(shop)
            found.append((price, shop))
        for item in found:
            heappush(heap, item)
        return [shop for _, shop in found]

    def rent(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        from heapq import heappush

        self.out.add((shop, movie))
        heappush(self.rented, (self.cost[(shop, movie)], shop, movie))

    def drop(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        from heapq import heappush

        self.out.discard((shop, movie))
        heappush(self.unrented[movie], (self.cost[(shop, movie)], shop))

    def report(self):
        """
        :rtype: List[List[int]]
        """
        from heapq import heappop, heappush

        found = []
        seen = set()
        while self.rented and len(found) < 5:
            price, shop, movie = heappop(self.rented)
            if (shop, movie) not in self.out or (shop, movie) in seen:
                continue
            seen.add((shop, movie))
            found.append((price, shop, movie))
        for item in found:
            heappush(self.rented, item)
        return [[shop, movie] for _, shop, movie in found]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
