# Author: Kaustav Ghosh
# 1094. Car Pooling
# https://leetcode.com/problems/car-pooling/

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        diff = [0] * 1001
        for num, start, end in trips:
            diff[start] += num
            diff[end] -= num
        current = 0
        for d in diff:
            current += d
            if current > capacity:
                return False
        return True
