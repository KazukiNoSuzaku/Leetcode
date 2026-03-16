# Author: Kaustav Ghosh
# Problem: First Unique Number (Premium)
# Approach: Ordered dict to track unique numbers efficiently

from collections import OrderedDict

class Solution(object):
    pass

class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.unique = OrderedDict()
        self.seen = set()
        for n in nums:
            self.add(n)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if self.unique:
            return next(iter(self.unique))
        return -1

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value in self.seen:
            if value in self.unique:
                del self.unique[value]
        else:
            self.seen.add(value)
            self.unique[value] = True
