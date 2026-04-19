# Author: Kaustav Ghosh
# 2349. Design a Number Container System
# https://leetcode.com/problems/design-a-number-container-system/
# Difficulty: Medium
#
# Two dicts: index->number and number->sorted set of indices (using SortedList).
# change() updates index, find() returns min index for a number.

from sortedcontainers import SortedList
from collections import defaultdict

class NumberContainers(object):

    def __init__(self):
        self.index_to_num = {}
        self.num_to_indices = defaultdict(SortedList)

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        if index in self.index_to_num:
            old_num = self.index_to_num[index]
            if old_num == number:
                return
            self.num_to_indices[old_num].remove(index)
        self.index_to_num[index] = number
        self.num_to_indices[number].add(index)

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        indices = self.num_to_indices[number]
        if indices:
            return indices[0]
        return -1
