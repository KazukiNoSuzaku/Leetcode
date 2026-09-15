# Author: Kaustav Ghosh
# Problem: Design a Food Rating System
# Approach: Keep each food's cuisine and current rating, plus a max-heap per cuisine keyed by (-rating, food) so that ties go to the lexicographically smaller name. changeRating pushes a fresh entry rather than updating, and highestRated first pops entries whose rating is stale

import heapq
from collections import defaultdict


class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.info = {}
        self.heaps = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.info[food] = (cuisine, rating)
            heapq.heappush(self.heaps[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        cuisine = self.info[food][0]
        self.info[food] = (cuisine, newRating)
        heapq.heappush(self.heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        heap = self.heaps[cuisine]
        while -heap[0][0] != self.info[heap[0][1]][1]:
            heapq.heappop(heap)
        return heap[0][1]
